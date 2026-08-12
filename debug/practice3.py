"""
Charta FDE — small end-to-end practice: STARTER CODE (no solution).
This is the most job-realistic style: parse -> aggregate -> sort -> format.
Fill in the function(s), run `python3 charta_fde_end_to_end_starter.py`.

You can write helper functions if you want — only top_clinics_by_revenue is tested.
"""
import csv
from collections import defaultdict

# ===========================================================================
# THE TASK
# ---------------------------------------------------------------------------
# You're handed a raw CSV string of claims (first line is the header):
#
#   clinic,amount,status
#   North Clinic,120.50,paid
#   South Clinic,80,denied
#   North Clinic,50,paid
#   ...
#
# Return the top `n` clinics by TOTAL PAID revenue, formatted as strings:
#
#   ["North Clinic: $170.50", "West Clinic: $95.00", ...]
#
# Rules:
#   - Only count rows where status == "paid". Ignore "denied"/other.
#   - Sum amounts per clinic. amount is a string in the CSV -> make it a float.
#   - Sort by total revenue DESC; break ties by clinic name ascending.
#   - Format each as "<clinic>: $<total>" with exactly 2 decimal places.
#   - Trim whitespace on fields. Skip blank lines. Don't crash on a short/bad row.
# ===========================================================================
def top_clinics_by_revenue(csv_text: str, n: int) -> list[str]:

    reader = csv.reader(csv_text.splitlines())
    rows = list(reader)  
    d = defaultdict(int)


    for row in rows:
        clinic = row[0].strip()      # strip whitespace so "  East Clinic " matches
        amount = row[1].strip()
        status = row[2].strip()
        if status == "paid":         # only paid rows count toward revenue
            d[clinic] += float(amount)
    
    # sorted(d.items(, key = lambda kv: (-kv[1], kv[0])))
    ranked = sorted(d.items(), key=lambda kv: (-kv[1], kv[0]))
    return [f"{clinic}: ${total:.2f}" for clinic, total in ranked[:n]]



def countRows(csv_text):
    rows = top_clinics_by_revenue(csv_text)
    count = 0

    for row in rows:
        if 'paid' in row:
            count += 1

def amountPerClinic():
    return




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

    csv1 = (
        "clinic,amount,status\n"
        "North Clinic,120.50,paid\n"
        "South Clinic,80,denied\n"
        "North Clinic,50,paid\n"
        "West Clinic,95,paid\n"
        "South Clinic,200,paid\n"
    )
    r.append(_check("top 2",
        top_clinics_by_revenue(csv1, 2),
        ["South Clinic: $200.00", "North Clinic: $170.50"]))

    # tie-break: two clinics tie at 100.00 -> alphabetical (Alpha before Beta)
    csv2 = (
        "clinic,amount,status\n"
        "Beta,100,paid\n"
        "Alpha,60,paid\n"
        "Alpha,40,paid\n"
    )
    r.append(_check("tie-break by name",
        top_clinics_by_revenue(csv2, 2),
        ["Alpha: $100.00", "Beta: $100.00"]))

    # messy input: blank line, extra spaces, a short/bad row that should be skipped
    csv3 = (
        "clinic,amount,status\n"
        "  East Clinic , 30 , paid \n"
        "\n"
        "North Clinic,70,paid\n"
        "broken row with no commas\n"
        "East Clinic,20,paid\n"
    )
    r.append(_check("messy input survives",
        top_clinics_by_revenue(csv3, 5),
        ["North Clinic: $70.00", "East Clinic: $50.00"]))

    print(f"\n{sum(r)}/{len(r)} checks passing")


if __name__ == "__main__":
    _run()