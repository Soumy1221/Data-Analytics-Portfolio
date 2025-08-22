# Flask UI for Financial Reconciliation
# Run: pip install -r requirements.txt && flask --app app run
import os
from flask import Flask, request, render_template_string, send_file
import pandas as pd

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Reconciliation Tool</title>
<h2>Upload two Excel files to reconcile</h2>
<form method=post enctype=multipart/form-data>
  <input type=file name=file1 required>
  <input type=file name=file2 required>
  <input type=submit value=Reconcile>
</form>
{% if report %}
  <p>Report generated:</p>
  <a href="/download">Download reconciliation_report.xlsx</a>
{% endif %}
"""

@app.route("/", methods=["GET","POST"])
def index():
    report_ready = False
    if request.method == "POST":
        f1 = request.files["file1"]
        f2 = request.files["file2"]
        a = pd.read_excel(f1)
        b = pd.read_excel(f2)
        merged = a.merge(b, on="TransactionID", how="outer", suffixes=("_A","_B"), indicator=True)
        amount_diff = merged[(~merged["Amount_A"].isna()) & (~merged["Amount_B"].isna()) & (merged["Amount_A"] != merged["Amount_B"])]
        only_in_a = merged[merged["_merge"] == "left_only"]
        only_in_b = merged[merged["_merge"] == "right_only"]
        with pd.ExcelWriter("reconciliation_report.xlsx") as writer:
            amount_diff.to_excel(writer, sheet_name="Amount_Differences", index=False)
            only_in_a.to_excel(writer, sheet_name="Only_in_FileA", index=False)
            only_in_b.to_excel(writer, sheet_name="Only_in_FileB", index=False)
        report_ready = True
    return render_template_string(HTML, report=report_ready)

@app.route("/download")
def download():
    return send_file("reconciliation_report.xlsx", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
