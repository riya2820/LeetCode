import re
# ===========================================================================
# B1 — Parse a delimited config string into a dict.
# Input like "region=us;retries=3;debug=true" -> {"region": "us",
#   "retries": "3", "debug": "true"}. Pairs split on ";", key/val on "=".
# Ignore empty chunks (e.g. trailing ";"). Trim whitespace around keys/vals.
# ===========================================================================
def parse_config(s: str) -> dict:
    d = {}
    i = 0
    charList = re.split(r'[=;]', s) # [ "retries", "3", "debug", "true"]
    
    while i in range(len(charList)-1):
        d[charList[i].strip()] = charList[i+1].strip()
        i += 2

    return d

# ===========================================================================
# B3 — Deduplicate encounters, keeping the LATEST per patient.
# Each record: {"patient_id": str, "date": "YYYY-MM-DD", "code": str}.
# If a patient appears twice, keep the one with the newer date.
# Return a list sorted by patient_id ascending.
# (dates are ISO strings, so string comparison works for "newer")
# ===========================================================================
def latest_per_patient(records: list[dict]) -> list[dict]:
    # TODO
    return None


# ===========================================================================
# B4 — Join two datasets on a shared key (enrich claims with patient name).
# claims: [{"claim_id", "patient_id", "amount"}]
# patients: [{"patient_id", "name"}]
# Return claims with a "name" field added. If no matching patient,
# name should be "UNKNOWN". Preserve original claim order.
# ===========================================================================
'''
patients = [
    {"patient_id": "p1", "name": "Alice"},
    {"patient_id": "p2", "name": "Bob"},
]

appointments = [
    {"patient_id": "p2", "date": "2026-07-20"},
    {"patient_id": "p1", "date": "2026-07-22"},
    {"patient_id": "p3", "date": "2026-07-23"},
]
[
    {
        "patient_id": "p2",
        "name": "Bob",
        "date": "2026-07-20"
    },
    {
        "patient_id": "p1",
        "name": "Alice",
        "date": "2026-07-22"
    }
]

patient_lookup = {
        patient["patient_id"]: patient
        for patient in patients
    }

    result = []

    for appointment in appointments:
        patient_id = appointment["patient_id"]

        if patient_id in patient_lookup:
            patient = patient_lookup[patient_id]

            result.append({
                "patient_id": patient_id,
                "name": patient["name"],
                "date": appointment["date"],
            })

    return result
'''
'''[{"claim_id": "c1", "patient_id": "p1", "amount": 100},
             {"claim_id": "c2", "patient_id": "p9", "amount": 50}],
            [{"patient_id": "p1", "name": "Ada"}]),
        [{"claim_id": "c1", "patient_id": "p1", "amount": 100, "name": "Ada"},
         {"claim_id": "c2", "patient_id": "p9", "amount": 50, "name": "UNKNOWN"}]))'''

def enrich_claims(claims: list[dict], patients: list[dict]) -> list[dict]:
    result = []

    patients_lookup = { # {p1" {...}, p2: {...}}
        patient["patient_id"]: patient
        for patient in patients
    }
    print(patients_lookup)

    for claim in claims:
        #if claim["patient_id"] in patients_lookup:
        result.append({ 
            "claim_id": claim["claim_id"],
            "patient_id": claim["patient_id"],
            "amount": claim["amount"],
            "name": patients_lookup.get(claim["patient_id"], {}).get("name", "UNKNOWN") #patients_lookup[claim["patient_id"]]["name"]
        })
        '''
        else:
            result.append({ 
                "claim_id": claim["claim_id"],
                "patient_id": claim["patient_id"],
                "amount": claim["amount"],
                "name": "UNKNOWN"
            })'''

    return result 
        

# ===========================================================================
# B5 — Batch a list into chunks of size k (for bulk API calls).
# chunk([1,2,3,4,5], 2) -> [[1,2],[3,4],[5]]. Last chunk may be smaller.
# k >= 1. Empty input -> [].
# ===========================================================================
def chunk(items: list, k: int) -> list[list]:
    # TODO
    return None


# ===========================================================================
# TEST HARNESS (don't edit — implement above to pass)
# ===========================================================================
def _check(name, got, want):
    ok = got == want
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if not ok:
        print(f"       got:  {got}")
        print(f"       want: {want}")
    return ok


def _run():
    r = []

    r.append(_check("B1 parse_config",
        parse_config("region=us; retries=3 ;debug=true;"),
        {"region": "us", "retries": "3", "debug": "true"}))

    r.append(_check("B3 latest_per_patient",
        latest_per_patient([
            {"patient_id": "p1", "date": "2026-01-01", "code": "A"},
            {"patient_id": "p1", "date": "2026-03-01", "code": "B"},  # newer
            {"patient_id": "p2", "date": "2026-02-01", "code": "C"},
        ]),
        [{"patient_id": "p1", "date": "2026-03-01", "code": "B"},
         {"patient_id": "p2", "date": "2026-02-01", "code": "C"}]))

    r.append(_check("B4 enrich_claims",
        enrich_claims(
            [{"claim_id": "c1", "patient_id": "p1", "amount": 100},
             {"claim_id": "c2", "patient_id": "p9", "amount": 50}],
            [{"patient_id": "p1", "name": "Ada"}]),
        [{"claim_id": "c1", "patient_id": "p1", "amount": 100, "name": "Ada"},
         {"claim_id": "c2", "patient_id": "p9", "amount": 50, "name": "UNKNOWN"}]))

    r.append(_check("B5 chunk", chunk([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]]))
    r.append(_check("B5 chunk empty", chunk([], 3), []))

    print(f"\n{sum(r)}/{len(r)} checks passing")


if __name__ == "__main__":
    _run()