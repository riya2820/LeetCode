from collections import defaultdict

def groupBySellers(records):
    d = defaultdict(lambda:{"item": [], "total": 0})

    for record in records:
        # {'seller': 'alice', 'item': 'shoes', 'price': 50}
        seller = record["seller"]
        d[seller]["item"].append(record["item"])
        d[seller]["total"] += record["price"]

    return dict(d.items())


# "alice": {"items": ["shoes"], "total": 50}
# new_record = {"seller": "alice", "item": "bag", "price": 80}
# {"alice": {"items": ["shoes", "bag"], "total": 130}}
def mergeRecord(records, new):
    seller = new["seller"]

    # for record in records.items(): inefficient! no need to loop thru the whole thing!
        # seller = new["seller"]
    if seller in records:
        records[seller]["item"].append(new["item"])
        records[seller]["total"] += new["price"]
    else:
        records[seller]["item"] = new["item"]
        records[seller]["total"] = new["price"]

    return records


def highestRevenue(records):
    groupedRecords = groupBySellers(records)
    return max(groupedRecords, key=lambda x: groupedRecords[x]['total'])



records = [
    {"seller": "alice", "item": "shoes", "price": 50},
    {"seller": "bob",   "item": "hat",   "price": 20},
    {"seller": "alice", "item": "bag",   "price": 80},
    {"seller": "bob",   "item": "belt",  "price": 30},
    {"seller": "alice", "item": "shoes", "price": 60},
]

print(groupBySellers(records))

existing = { "alice": {"item": ["shoes"], "total": 50} }
new_record = {"seller": "alice", "item": "bag", "price": 80}

# Expected after merge:
# {"alice": {"items": ["shoes", "bag"], "total": 130}}
print(mergeRecord(existing, new_record))
print(highestRevenue(records))
'''

counter = 0

def increment():
    global counter
    for _ in range(100000):
        counter += 1

t1 = threading.Thread(target=increment)
t2 = threading.Thread(target=increment)
t1.start(); t2.start()
t1.join(); t2.join()
print(counter)  # Expected: 200000


def foo(x):
    lst = []
    lst.append(x)
    return lst

print(foo(1))
print(foo(2))
print(foo(3))

def twoSum(nums, target):
    for num in nums:
        if target-num in nums:
            return True

    return False 

nums = [-3, 1, 4, 9]
target = 7
print(twoSum(nums, target))


def mystery(nums):
    seen = {}
    for i, n in enumerate(nums):
        if n in seen: 
            return [seen[n], i] # 
        seen[-n] = i# {-3:0, -5:1,  3:2} 
                    # {-2:0, -7:1, -11:2, -12:3}
                    # {-1:0, -2:1, -3:3}
    return []


def has_duplicates(nums):
    seen = {}
    for num in nums:
        if num in seen.values(): # issue here, also could simply use values 
            return True
        seen[num] = True
    return False


print(mystery([2, 7, 11, 15]))  # Case A
print(mystery([3, 5, -3]))      # Case B
print(mystery([1, 2, 3]))       # Case C
print(mystery([-5, 5]))         # Case D
print(mystery([]))              # Case E
'''