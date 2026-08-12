"""
TRADE DESK OA PREP — CodeSignal Industry Coding Framework (ICF) style
=====================================================================
Format they actually use: 90 min, ONE stateful system, 4 progressive levels.
You implement a class; each level layers on top of your previous code.
Scoring is per-level and cumulative — Level 1 & 2 are cheap points, do NOT
rush them. Most people lose the OA by never reaching Level 4, not by writing
elegant code.

WHAT IS ACTUALLY TESTED (based on reported TTD/Coinbase/Anthropic ICF sets):
  L1  basic CRUD on a dict-of-dicts, return None/False on invalid input
  L2  top-K ranking with tie-breaking (count desc, then id ASC), prefix scans
  L3  timestamps: TTL / expiry / scheduled ops / time-windowed queries
  L4  merge two entities, or cancel/rollback with cascading side effects

STRATEGY NOTES FOR THE REAL THING:
  - Model state as dicts from the start. Every level-4 twist is easier if L1
    stored a dict instead of a list.
  - Expiry convention is almost always EXCLUSIVE: alive if now < expire_ts.
  - Tie-break convention is almost always: value DESC, then key ASC.
  - Write helper methods (_purge, _process). L3/L4 will need them and the
    graders reward readable decomposition.
  - Return format is usually "id(value)" strings, not tuples. Read it twice.

HOW TO USE THIS FILE:
  Fill in each `raise NotImplementedError`. Run `python ttd_practice.py`.
  It runs problems in order and STOPS at the first failure so you get one
  clear target at a time. Hints are one line above each method — read them
  only if you're stuck. Tests are the spec: they encode every edge case.

  Run a single problem while iterating:  python ttd_practice.py 4
  All test expectations here have been verified against a working solution.

Suggested order: P1 (the exact reported TTD problem) -> P2 -> P3, then pick.
Time yourself: 20 min per problem is roughly OA pace.
"""

from typing import Optional, List
import heapq
import sys

DAY = 86_400_000  # ms in 24h


# =====================================================================
# P1 — BANKING SYSTEM   *** the problem TTD candidates report most often ***
# =====================================================================
class BankingSystem:
    """
    L1: create_account, deposit, transfer, get_balance
    L2: top_spenders  (ranked by TOTAL OUTGOING money, not balance)
    L3: schedule_payment / cancel_payment, with 2% cashback 24h after execution
    L4: merge_accounts

    Timestamps (ts) are milliseconds and are non-decreasing across calls.
    Scheduled payments must be processed LAZILY: at the start of every public
    call, first execute every pending event whose time <= ts. A payment only
    goes through if the balance is sufficient AT EXECUTION TIME; otherwise it
    is dropped. Cashback = floor(amount * 2 / 100), credited at exec_ts + DAY.
    Payment ids are "payment1", "payment2", ... in creation order, globally.
    """

    def __init__(self):
        # HINT: accounts dict {balance, outgoing}, a min-heap of pending events
        # (time, seq, kind, payment_id), a payments dict, and two counters.
        raise NotImplementedError

    # HINT: pop every event with time <= ts, in (time, creation order); handle
    # "exec" (withdraw if funded -> schedule cashback, else drop) and "cashback".
    def _process(self, ts: int) -> None:
        raise NotImplementedError

    # HINT: False if the id already exists.
    def create_account(self, ts: int, account_id: str) -> bool:
        raise NotImplementedError

    # HINT: return the new balance, or None if the account doesn't exist.
    def deposit(self, ts: int, account_id: str, amount: int) -> Optional[int]:
        raise NotImplementedError

    # HINT: None if either account is missing, source == target, or underfunded.
    # A transfer counts toward the source's outgoing total.
    def transfer(self, ts: int, source: str, target: str, amount: int) -> Optional[int]:
        raise NotImplementedError

    # HINT: None if missing.
    def get_balance(self, ts: int, account_id: str) -> Optional[int]:
        raise NotImplementedError

    # HINT: ["acc(500)", ...] sorted by outgoing DESC then account_id ASC.
    # Accounts with zero outgoing still appear.
    def top_spenders(self, ts: int, n: int) -> List[str]:
        raise NotImplementedError

    # HINT: None if account missing OR balance < amount right now. Otherwise
    # mint an id, record it as pending, and push an "exec" event at ts + delay.
    def schedule_payment(self, ts: int, account_id: str, amount: int, delay: int) -> Optional[str]:
        raise NotImplementedError

    # HINT: True only if the payment exists, belongs to this account, and is
    # still pending (not already executed or cancelled).
    def cancel_payment(self, ts: int, account_id: str, payment_id: str) -> bool:
        raise NotImplementedError

    # HINT: fold id2 into id1 — balances add, outgoing totals add, id2's pending
    # payments AND pending cashbacks now belong to id1, then delete id2.
    def merge_accounts(self, ts: int, id1: str, id2: str) -> bool:
        raise NotImplementedError


# =====================================================================
# P2 — IN-MEMORY DB (key -> field -> value)
# =====================================================================
class InMemoryDB:
    """
    L1: set/get/delete a field on a record
    L2: scan / scan_by_prefix -> ["field(value)"] sorted by field name
    L3: the *_at family — every op takes a timestamp, plus TTL support
    L4: (bonus, no tests) backup(ts) / restore(ts, ts_to_restore)

    A field written with a TTL is alive while  ts < created_ts + ttl.
    Overwriting a TTL'd field with a plain set makes it permanent again.
    """

    def __init__(self):
        # HINT: {key: {field: (value, expire_ts_or_None)}}
        raise NotImplementedError

    # HINT: expire_ts is None -> permanent.
    def set_at(self, key: str, field: str, value: str, ts: int) -> None:
        raise NotImplementedError

    def set_at_with_ttl(self, key: str, field: str, value: str, ts: int, ttl: int) -> None:
        raise NotImplementedError

    # HINT: None if missing OR expired. Expiry is EXCLUSIVE (dead at exactly exp).
    def get_at(self, key: str, field: str, ts: int) -> Optional[str]:
        raise NotImplementedError

    # HINT: deleting an already-expired field returns False.
    def delete_at(self, key: str, field: str, ts: int) -> bool:
        raise NotImplementedError

    # HINT: this is just scan_by_prefix_at with an empty prefix — don't duplicate.
    def scan_at(self, key: str, ts: int) -> List[str]:
        raise NotImplementedError

    # HINT: filter by startswith AND liveness, format "field(value)", sort.
    def scan_by_prefix_at(self, key: str, prefix: str, ts: int) -> List[str]:
        raise NotImplementedError


# =====================================================================
# P3 — CLOUD STORAGE
# =====================================================================
class CloudStorage:
    """
    L1: add_file / get_file_size / delete_file
    L2: get_n_largest(prefix, n)
    L3: add_user with a capacity cap; add_file_by charges the user's quota
    L4: merge_user — u2's files and capacity fold into u1

    Files added via add_file belong to "admin", who has infinite capacity.
    Deleting a file refunds its owner's used quota.
    """

    def __init__(self):
        # HINT: files {name: (size, owner)}, users {id: {cap, used}} with admin
        # pre-created at capacity float("inf").
        raise NotImplementedError

    # HINT: this is just add_file_by("admin", ...) — reuse it.
    def add_file(self, name: str, size: int) -> bool:
        raise NotImplementedError

    def get_file_size(self, name: str) -> Optional[int]:
        raise NotImplementedError

    # HINT: return the freed size and give the quota back to the owner.
    def delete_file(self, name: str) -> Optional[int]:
        raise NotImplementedError

    # HINT: ["name(size)"] sorted size DESC then name ASC; [] if no match.
    def get_n_largest(self, prefix: str, n: int) -> List[str]:
        raise NotImplementedError

    # HINT: False if the id is taken (including "admin").
    def add_user(self, user_id: str, capacity: int) -> bool:
        raise NotImplementedError

    # HINT: None if user missing, name already taken, or used + size > cap.
    # Otherwise return REMAINING capacity (return -1 for admin's infinity).
    def add_file_by(self, user_id: str, name: str, size: int) -> Optional[int]:
        raise NotImplementedError

    # HINT: reassign u2's files to u1, add capacities and used, delete u2,
    # return u1's new remaining capacity. None if same id, missing, or admin.
    def merge_user(self, user_id_1: str, user_id_2: str) -> Optional[int]:
        raise NotImplementedError


# =====================================================================
# P4 — AD CAMPAIGN MANAGER  (ad-tech flavored — closest to TTD's domain)
# =====================================================================
class AdCampaignManager:
    """
    L1: create_campaign(budget), record_impression(cost), get_spend
    L2: top_campaigns(n)
    L3: pause_campaign / resume_campaign
    L4: spend_in_window(campaign, start_ts, end_ts)  [inclusive both ends]

    An impression that would push spend OVER budget is REJECTED outright
    (not clipped). Paused campaigns reject all impressions.
    """

    def __init__(self):
        raise NotImplementedError

    def create_campaign(self, campaign_id: str, budget: int) -> bool:
        raise NotImplementedError

    # HINT: False if missing, paused, or spend + cost > budget. Keep the
    # (ts, cost) history — L4 needs it.
    def record_impression(self, ts: int, campaign_id: str, cost: int) -> bool:
        raise NotImplementedError

    def get_spend(self, campaign_id: str) -> Optional[int]:
        raise NotImplementedError

    # HINT: "id(spend)", spend DESC then id ASC. Zero-spend campaigns included.
    def top_campaigns(self, n: int) -> List[str]:
        raise NotImplementedError

    # HINT: False if missing or already in that state.
    def pause_campaign(self, campaign_id: str) -> bool:
        raise NotImplementedError

    def resume_campaign(self, campaign_id: str) -> bool:
        raise NotImplementedError

    # HINT: sum costs where start_ts <= ts <= end_ts. None if campaign missing.
    def spend_in_window(self, campaign_id: str, start_ts: int, end_ts: int) -> Optional[int]:
        raise NotImplementedError


# =====================================================================
# P5 — BID RATE LIMITER  (sliding window)
# =====================================================================
class BidRateLimiter:
    """
    L1: register_client(limit), allow(ts, client)
    L2: count(ts, client) — live requests in the current window
    L3: set_global_limit — a cap across ALL clients combined
    L4: refund(ts, client) — undo the most recent still-live request

    Window is (ts - window_ms, ts]: a request at time t is live iff
    t > ts - window_ms. Unregistered clients are always denied.
    """

    def __init__(self, window_ms: int):
        # HINT: limits {client: n}, log {client: [timestamps]}, global_limit=None
        raise NotImplementedError

    # HINT: drop timestamps <= ts - window_ms from every client's log.
    def _evict(self, ts: int) -> None:
        raise NotImplementedError

    def register_client(self, client_id: str, limit: int) -> bool:
        raise NotImplementedError

    def set_global_limit(self, limit: int) -> None:
        raise NotImplementedError

    # HINT: evict first, then check the per-client limit, THEN the global limit
    # (sum of all live logs). Only append if both pass.
    def allow(self, ts: int, client_id: str) -> bool:
        raise NotImplementedError

    # HINT: None for unregistered clients (not 0).
    def count(self, ts: int, client_id: str) -> Optional[int]:
        raise NotImplementedError

    # HINT: pop the newest live timestamp. False if nothing live to refund.
    def refund(self, ts: int, client_id: str) -> bool:
        raise NotImplementedError


# =====================================================================
# P6 — INVENTORY MANAGER  (stock vs. available, TTL reservations)
# =====================================================================
class InventoryManager:
    """
    L1: add_stock / remove_stock / get_qty
    L2: search_by_prefix
    L3: reserve(ts, sku, qty, ttl) -> "res1", "res2", ... ; expiring holds
    L4: available(ts, sku) = stock - live reservations ; release(ts, rid)

    A reservation does NOT reduce stock, only availability. Reservations
    expire EXCLUSIVELY: dead at exactly ts == created + ttl.
    """

    def __init__(self):
        raise NotImplementedError

    # HINT: drop reservations whose exp <= ts. Call this at the top of every
    # time-aware method.
    def _purge(self, ts: int) -> None:
        raise NotImplementedError

    def add_stock(self, sku: str, qty: int) -> int:
        raise NotImplementedError

    # HINT: None if sku missing or stock < qty.
    def remove_stock(self, sku: str, qty: int) -> Optional[int]:
        raise NotImplementedError

    def get_qty(self, sku: str) -> Optional[int]:
        raise NotImplementedError

    # HINT: sorted list of sku names, not "sku(qty)" strings. Read the test.
    def search_by_prefix(self, prefix: str) -> List[str]:
        raise NotImplementedError

    # HINT: stock minus the sum of live reservation quantities for that sku.
    def available(self, ts: int, sku: str) -> Optional[int]:
        raise NotImplementedError

    # HINT: None if sku missing or available < qty. Ids are global: res1, res2...
    def reserve(self, ts: int, sku: str, qty: int, ttl: int) -> Optional[str]:
        raise NotImplementedError

    # HINT: releasing an already-expired or unknown reservation is False.
    def release(self, ts: int, reservation_id: str) -> bool:
        raise NotImplementedError


# =====================================================================
# P7 — VERSIONED KEY-VALUE STORE
# =====================================================================
class VersionedStore:
    """
    L1: put -> returns a GLOBAL monotonically increasing version number; get
    L2: get_at_version(key, version) — the value as of that version
    L3: history(key) -> ["version(value)"] in ascending version order
    L4: rollback(key, version) — re-put the old value as a NEW version

    The version counter is shared across all keys. get_at_version(k, v) means:
    the last write to k with version <= v. None if k had no write by then.
    """

    def __init__(self):
        # HINT: {key: [(version, value), ...]} kept in ascending version order.
        raise NotImplementedError

    def put(self, key: str, value: str) -> int:
        raise NotImplementedError

    def get(self, key: str) -> Optional[str]:
        raise NotImplementedError

    # HINT: walk (or binary search) the key's list for the last version <= v.
    def get_at_version(self, key: str, version: int) -> Optional[str]:
        raise NotImplementedError

    def history(self, key: str) -> List[str]:
        raise NotImplementedError

    # HINT: rollback is get_at_version + put. It does NOT erase history.
    # None if there's no value at/before that version.
    def rollback(self, key: str, version: int) -> Optional[int]:
        raise NotImplementedError


# =====================================================================
# P8 — TASK SCHEDULER  (the one graph-ish problem — worth 20 min)
# =====================================================================
class TaskScheduler:
    """
    L1: add_task(id, duration)
    L2: add_dependency(task, depends_on) — must REJECT cycles
    L3: order() — topological, ties broken alphabetically
    L4: min_completion_time() (unlimited parallelism = critical path),
        cancel_task() with cascading removal of everything downstream
    """

    def __init__(self):
        # HINT: dur {}, deps {t: set(prereqs)}, rdeps {t: set(dependents)}.
        # Keeping BOTH directions is what makes L4 cheap.
        raise NotImplementedError

    def add_task(self, task_id: str, duration: int) -> bool:
        raise NotImplementedError

    # HINT: adding task<-depends_on creates a cycle iff depends_on already
    # (transitively) depends on task. DFS the deps graph to check.
    def add_dependency(self, task_id: str, depends_on: str) -> bool:
        raise NotImplementedError

    # HINT: Kahn's algorithm with a MIN-HEAP instead of a queue — that's what
    # gives you the alphabetical tie-break for free.
    def order(self) -> List[str]:
        raise NotImplementedError

    # HINT: walk order(); finish[t] = max(finish[prereqs], default 0) + dur[t];
    # answer is max(finish.values()).
    def min_completion_time(self) -> int:
        raise NotImplementedError

    # HINT: BFS/DFS the REVERSE graph to collect everything downstream, delete
    # them all, and scrub the deleted ids out of surviving tasks' edge sets.
    # Return the removed ids sorted.
    def cancel_task(self, task_id: str) -> List[str]:
        raise NotImplementedError


# =====================================================================
# P9 — LOG AGGREGATOR
# =====================================================================
class LogAggregator:
    """
    L1: ingest(ts, source, level, message), count(level)
    L2: query(start_ts, end_ts, level=None) -> ["ts:source:message"]
    L3: top_sources(n)
    L4: dedupe() — collapse duplicate (source, message) pairs, KEEPING the
        earliest timestamp; returns how many rows were removed.

    Logs may arrive out of order. query() results are sorted by ts, then source.
    """

    def __init__(self):
        raise NotImplementedError

    def ingest(self, ts: int, source: str, level: str, message: str) -> None:
        raise NotImplementedError

    def count(self, level: str) -> int:
        raise NotImplementedError

    # HINT: inclusive on both ends; level=None means all levels.
    def query(self, start_ts: int, end_ts: int, level: Optional[str] = None) -> List[str]:
        raise NotImplementedError

    # HINT: "source(count)", count DESC then source ASC.
    def top_sources(self, n: int) -> List[str]:
        raise NotImplementedError

    # HINT: sort by ts first, then keep the first occurrence of each
    # (source, message). Mutates state — count() must reflect it afterward.
    def dedupe(self) -> int:
        raise NotImplementedError


# =====================================================================
# P10 — GRID DRILLS  (a minority of candidates get the plain GCA instead,
#                     which reportedly includes one matrix question)
# =====================================================================

# HINT: 2D prefix sum, then slide the k x k box. None if the grid is empty
# or k doesn't fit. Watch out: sums can be negative, so don't init best = 0.
def max_kxk_sum(grid: List[List[int]], k: int) -> Optional[int]:
    raise NotImplementedError


# HINT: transpose in place, then reverse each row. Square grid. Return it too.
def rotate_90(grid: List[List[int]]) -> List[List[int]]:
    raise NotImplementedError


# HINT: count connected components of 1s, 4-directional, iterative DFS with an
# explicit stack (recursion blows up on big grids).
def region_count(grid: List[List[int]]) -> int:
    raise NotImplementedError


# =====================================================================
# TESTS — do not edit. These are the spec.
# =====================================================================

def t1():
    b = BankingSystem()
    assert b.create_account(1, "acc1") is True
    assert b.create_account(2, "acc1") is False
    assert b.create_account(3, "acc2") is True
    assert b.deposit(4, "acc1", 2000) == 2000
    assert b.deposit(5, "ghost", 100) is None
    assert b.transfer(6, "acc1", "acc2", 500) == 1500
    assert b.transfer(7, "acc1", "acc1", 10) is None
    assert b.transfer(8, "acc1", "acc2", 99999) is None
    assert b.transfer(9, "acc1", "ghost", 10) is None
    assert b.get_balance(10, "acc2") == 500

    assert b.top_spenders(11, 3) == ["acc1(500)", "acc2(0)"]
    b.create_account(12, "acc3")
    assert b.top_spenders(13, 3) == ["acc1(500)", "acc2(0)", "acc3(0)"]

    p1 = b.schedule_payment(100, "acc1", 300, 3000)
    assert p1 == "payment1"
    assert b.schedule_payment(101, "acc1", 999999, 10) is None      # underfunded now
    assert b.schedule_payment(102, "ghost", 10, 10) is None
    p2 = b.schedule_payment(103, "acc1", 100, 5000)
    assert p2 == "payment2"
    assert b.cancel_payment(104, "acc1", p2) is True
    assert b.cancel_payment(105, "acc1", p2) is False               # already cancelled
    assert b.cancel_payment(106, "acc2", p1) is False               # wrong owner

    assert b.get_balance(3000, "acc1") == 1500                      # not executed yet
    assert b.get_balance(3100, "acc1") == 1200                      # exec at 100+3000
    assert b.top_spenders(3100, 1) == ["acc1(800)"]
    assert b.get_balance(3100 + DAY - 1, "acc1") == 1200            # cashback not yet
    assert b.get_balance(3100 + DAY, "acc1") == 1206                # 2% of 300 = 6
    assert b.cancel_payment(3100 + DAY, "acc1", p1) is False        # already executed

    ts = 10 * DAY
    assert b.merge_accounts(ts, "acc1", "acc1") is False
    assert b.merge_accounts(ts, "acc1", "ghost") is False
    assert b.merge_accounts(ts, "acc1", "acc2") is True
    assert b.get_balance(ts, "acc2") is None
    assert b.get_balance(ts, "acc1") == 1706                        # 1206 + acc2's 500
    assert b.top_spenders(ts, 5) == ["acc1(800)", "acc3(0)"]
    print("P1 BankingSystem OK")


def t2():
    d = InMemoryDB()
    d.set_at("u1", "name", "riya", 1)
    d.set_at("u1", "city", "sf", 1)
    assert d.get_at("u1", "name", 2) == "riya"
    assert d.get_at("u1", "zzz", 2) is None
    assert d.get_at("ghost", "name", 2) is None
    assert d.delete_at("u1", "city", 3) is True
    assert d.delete_at("u1", "city", 4) is False
    assert d.get_at("u1", "city", 5) is None

    d.set_at("u1", "role", "eng", 6)
    d.set_at("u1", "region", "west", 6)
    assert d.scan_at("u1", 7) == ["name(riya)", "region(west)", "role(eng)"]
    assert d.scan_by_prefix_at("u1", "r", 7) == ["region(west)", "role(eng)"]
    assert d.scan_at("ghost", 7) == []

    d.set_at_with_ttl("u2", "session", "abc", 10, 100)   # expires at 110
    assert d.get_at("u2", "session", 50) == "abc"
    assert d.get_at("u2", "session", 109) == "abc"
    assert d.get_at("u2", "session", 110) is None        # exclusive expiry
    assert d.scan_at("u2", 110) == []
    assert d.delete_at("u2", "session", 110) is False

    d.set_at_with_ttl("u3", "k", "v1", 10, 5)
    assert d.get_at("u3", "k", 14) == "v1"
    d.set_at("u3", "k", "v2", 12)                        # overwrite kills the TTL
    assert d.get_at("u3", "k", 1000) == "v2"
    print("P2 InMemoryDB OK")


def t3():
    c = CloudStorage()
    assert c.add_file("/dir/f1.txt", 100) is True
    assert c.add_file("/dir/f1.txt", 200) is False
    assert c.get_file_size("/dir/f1.txt") == 100
    assert c.get_file_size("/nope") is None
    assert c.delete_file("/nope") is None

    c.add_file("/dir/f2.txt", 300)
    c.add_file("/dir/f3.txt", 300)
    c.add_file("/other/f4.txt", 500)
    assert c.get_n_largest("/dir", 3) == ["/dir/f2.txt(300)", "/dir/f3.txt(300)", "/dir/f1.txt(100)"]
    assert c.get_n_largest("/dir", 1) == ["/dir/f2.txt(300)"]
    assert c.get_n_largest("/zzz", 2) == []
    assert c.delete_file("/dir/f2.txt") == 300

    assert c.add_user("u1", 1000) is True
    assert c.add_user("u1", 5000) is False
    assert c.add_user("admin", 5) is False
    assert c.add_file_by("u1", "/u1/a", 400) == 600
    assert c.add_file_by("u1", "/u1/b", 700) is None      # over capacity
    assert c.add_file_by("u1", "/dir/f1.txt", 10) is None # name collision
    assert c.add_file_by("ghost", "/x", 1) is None
    assert c.delete_file("/u1/a") == 400
    assert c.add_file_by("u1", "/u1/c", 900) == 100       # quota was refunded

    c.add_user("u2", 500)
    c.add_file_by("u2", "/u2/a", 200)
    assert c.merge_user("u1", "u2") == 400                # (1000+500) - (900+200)
    assert c.merge_user("u1", "u2") is None
    assert c.merge_user("u1", "admin") is None
    assert c.get_file_size("/u2/a") == 200                # file survives the merge
    print("P3 CloudStorage OK")


def t4():
    m = AdCampaignManager()
    assert m.create_campaign("c1", 1000) is True
    assert m.create_campaign("c1", 5) is False
    m.create_campaign("c2", 400)
    assert m.record_impression(10, "c1", 300) is True
    assert m.record_impression(20, "c1", 300) is True
    assert m.record_impression(30, "c1", 500) is False    # would exceed budget
    assert m.record_impression(30, "ghost", 1) is False
    assert m.get_spend("c1") == 600
    assert m.get_spend("ghost") is None

    assert m.record_impression(40, "c2", 400) is True
    assert m.top_campaigns(2) == ["c1(600)", "c2(400)"]
    m.create_campaign("c0", 100)
    m.record_impression(50, "c0", 400)                    # rejected, spend stays 0
    assert m.get_spend("c0") == 0
    assert m.top_campaigns(5) == ["c1(600)", "c2(400)", "c0(0)"]

    assert m.pause_campaign("c1") is True
    assert m.pause_campaign("c1") is False
    assert m.record_impression(60, "c1", 10) is False
    assert m.resume_campaign("c1") is True
    assert m.record_impression(70, "c1", 10) is True
    assert m.get_spend("c1") == 610

    assert m.spend_in_window("c1", 10, 20) == 600
    assert m.spend_in_window("c1", 11, 20) == 300
    assert m.spend_in_window("c1", 0, 5) == 0
    assert m.spend_in_window("ghost", 0, 100) is None
    print("P4 AdCampaignManager OK")


def t5():
    r = BidRateLimiter(1000)
    assert r.register_client("dsp1", 3) is True
    assert r.register_client("dsp1", 9) is False
    assert r.allow(0, "ghost") is False

    assert r.allow(100, "dsp1") is True
    assert r.allow(200, "dsp1") is True
    assert r.allow(300, "dsp1") is True
    assert r.allow(400, "dsp1") is False      # limit of 3 in the window
    assert r.count(400, "dsp1") == 3
    assert r.allow(1100, "dsp1") is True      # the 100 request has aged out
    assert r.count(1100, "dsp1") == 3
    assert r.count(1400, "dsp1") == 1         # only the 1100 request survives
    assert r.count(1400, "ghost") is None

    assert r.refund(1400, "dsp1") is True
    assert r.count(1400, "dsp1") == 0
    assert r.refund(1400, "dsp1") is False
    assert r.refund(1400, "ghost") is False

    g = BidRateLimiter(1000)
    g.register_client("a", 5)
    g.register_client("b", 5)
    g.set_global_limit(3)
    assert g.allow(10, "a") is True
    assert g.allow(20, "a") is True
    assert g.allow(30, "b") is True
    assert g.allow(40, "b") is False          # global cap, not the per-client one
    assert g.allow(1050, "b") is True         # a's two requests aged out
    print("P5 BidRateLimiter OK")


def t6():
    i = InventoryManager()
    assert i.add_stock("sku-a", 10) == 10
    assert i.add_stock("sku-a", 5) == 15
    assert i.get_qty("sku-a") == 15
    assert i.get_qty("ghost") is None
    assert i.remove_stock("sku-a", 20) is None
    assert i.remove_stock("sku-a", 5) == 10
    assert i.remove_stock("ghost", 1) is None

    i.add_stock("sku-b", 3)
    i.add_stock("other", 1)
    assert i.search_by_prefix("sku") == ["sku-a", "sku-b"]
    assert i.search_by_prefix("z") == []

    assert i.available(100, "sku-a") == 10
    r1 = i.reserve(100, "sku-a", 4, 500)      # expires at 600
    assert r1 == "res1"
    assert i.available(100, "sku-a") == 6
    assert i.get_qty("sku-a") == 10           # stock is untouched by a hold
    assert i.reserve(100, "sku-a", 7, 500) is None
    assert i.reserve(100, "ghost", 1, 500) is None
    r2 = i.reserve(200, "sku-a", 6, 100)      # expires at 300
    assert r2 == "res2"
    assert i.available(200, "sku-a") == 0
    assert i.available(300, "sku-a") == 6     # r2 expired (exclusive)
    assert i.release(300, r1) is True
    assert i.release(300, r1) is False
    assert i.available(300, "sku-a") == 10
    print("P6 InventoryManager OK")


def t7():
    v = VersionedStore()
    assert v.put("a", "1") == 1
    assert v.put("b", "x") == 2                # version counter is GLOBAL
    assert v.put("a", "2") == 3
    assert v.get("a") == "2"
    assert v.get("ghost") is None

    assert v.get_at_version("a", 1) == "1"
    assert v.get_at_version("a", 2) == "1"      # no write to 'a' at v2
    assert v.get_at_version("a", 3) == "2"
    assert v.get_at_version("a", 99) == "2"
    assert v.get_at_version("b", 1) is None     # 'b' didn't exist yet
    assert v.get_at_version("ghost", 5) is None

    assert v.history("a") == ["1(1)", "3(2)"]
    assert v.history("ghost") == []

    assert v.rollback("a", 1) == 4              # creates a NEW version
    assert v.get("a") == "1"
    assert v.history("a") == ["1(1)", "3(2)", "4(1)"]
    assert v.rollback("b", 1) is None
    assert v.rollback("ghost", 1) is None
    print("P7 VersionedStore OK")


def t8():
    s = TaskScheduler()
    assert s.add_task("a", 3) is True
    assert s.add_task("a", 9) is False
    s.add_task("b", 2); s.add_task("c", 4); s.add_task("d", 1)

    assert s.add_dependency("b", "a") is True
    assert s.add_dependency("c", "a") is True
    assert s.add_dependency("d", "b") is True
    assert s.add_dependency("d", "c") is True
    assert s.add_dependency("a", "d") is False    # cycle
    assert s.add_dependency("a", "a") is False
    assert s.add_dependency("b", "a") is False    # duplicate
    assert s.add_dependency("b", "ghost") is False

    assert s.order() == ["a", "b", "c", "d"]
    assert s.min_completion_time() == 8           # critical path a(3)->c(4)->d(1)

    s.add_task("z", 100)                          # independent
    assert s.min_completion_time() == 100
    assert s.order() == ["a", "b", "c", "d", "z"] # lexicographic among ready tasks

    assert s.cancel_task("ghost") == []
    assert s.cancel_task("a") == ["a", "b", "c", "d"]   # cascades downstream
    assert s.order() == ["z"]
    assert s.min_completion_time() == 100
    print("P8 TaskScheduler OK")


def t9():
    a = LogAggregator()
    a.ingest(5, "bid-svc", "ERROR", "timeout")
    a.ingest(1, "bid-svc", "INFO", "start")
    a.ingest(3, "feed-svc", "ERROR", "bad row")
    a.ingest(9, "bid-svc", "ERROR", "timeout")
    a.ingest(7, "feed-svc", "WARN", "slow")

    assert a.count("ERROR") == 3
    assert a.count("DEBUG") == 0

    assert a.query(1, 5) == ["1:bid-svc:start", "3:feed-svc:bad row", "5:bid-svc:timeout"]
    assert a.query(1, 5, "ERROR") == ["3:feed-svc:bad row", "5:bid-svc:timeout"]
    assert a.query(100, 200) == []

    assert a.top_sources(2) == ["bid-svc(3)", "feed-svc(2)"]
    a.ingest(11, "zz-svc", "INFO", "hi")
    a.ingest(12, "aa-svc", "INFO", "hi")
    assert a.top_sources(4) == ["bid-svc(3)", "feed-svc(2)", "aa-svc(1)", "zz-svc(1)"]

    assert a.dedupe() == 1                    # (bid-svc, timeout) twice; keeps ts=5
    assert a.count("ERROR") == 2
    assert a.query(0, 100, "ERROR") == ["3:feed-svc:bad row", "5:bid-svc:timeout"]
    assert a.dedupe() == 0
    print("P9 LogAggregator OK")


def t10():
    g = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]
    assert max_kxk_sum(g, 1) == 9
    assert max_kxk_sum(g, 2) == 28            # bottom-right 2x2
    assert max_kxk_sum(g, 3) == 45
    assert max_kxk_sum(g, 4) is None
    assert max_kxk_sum([], 1) is None
    assert max_kxk_sum([[-1, -2], [-3, -4]], 2) == -10   # all negative

    r = [[1, 2], [3, 4]]
    assert rotate_90(r) == [[3, 1], [4, 2]]
    r2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert rotate_90(r2) == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    grid = [[1, 1, 0, 0],
            [1, 0, 0, 1],
            [0, 0, 1, 1],
            [0, 1, 0, 0]]
    assert region_count(grid) == 3
    assert region_count([[0, 0], [0, 0]]) == 0
    assert region_count([]) == 0
    print("P10 grid drills OK")


TESTS = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        TESTS[int(sys.argv[1]) - 1]()
    else:
        for fn in TESTS:
            fn()
        print("\nall 10 passed")