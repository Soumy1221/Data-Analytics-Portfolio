# Automated Financial Reconciliation Tool

Compare two Excel ledgers and generate a reconciliation report.

## Quick Start (CLI)
```bash
pip install -r requirements.txt
python reconcile.py ledger_A.xlsx ledger_B.xlsx
```

This produces `reconciliation_report.xlsx` with:
- `Amount_Differences`: transactions with same ID but different amounts
- `Only_in_FileA`: present in File A only
- `Only_in_FileB`: present in File B only

## Web UI (Flask)
```bash
pip install -r requirements.txt
flask --app app run
```
Open `http://127.0.0.1:5000`, upload two Excel files, and download the report.
