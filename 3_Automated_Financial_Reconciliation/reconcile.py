# Financial Reconciliation Tool
# Run: python reconcile.py ledger_A.xlsx ledger_B.xlsx
import sys
import pandas as pd

if len(sys.argv) < 3:
    print("Usage: python reconcile.py file1.xlsx file2.xlsx")
    sys.exit(1)

file1, file2 = sys.argv[1], sys.argv[2]
a = pd.read_excel(file1)
b = pd.read_excel(file2)

# Merge on TransactionID to find mismatches and uniques
merged = a.merge(b, on="TransactionID", how="outer", suffixes=("_A","_B"), indicator=True)

# Identify issues
amount_diff = merged[(~merged["Amount_A"].isna()) & (~merged["Amount_B"].isna()) & (merged["Amount_A"] != merged["Amount_B"])]
only_in_a = merged[merged["_merge"] == "left_only"]
only_in_b = merged[merged["_merge"] == "right_only"]

with pd.ExcelWriter("reconciliation_report.xlsx") as writer:
    amount_diff.to_excel(writer, sheet_name="Amount_Differences", index=False)
    only_in_a.to_excel(writer, sheet_name="Only_in_FileA", index=False)
    only_in_b.to_excel(writer, sheet_name="Only_in_FileB", index=False)

print("Saved reconciliation_report.xlsx")
