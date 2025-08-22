# Customer Churn Prediction

Predict customer churn using Logistic Regression on a **synthetic Telco** dataset (structure inspired by the public Telco churn dataset).

## Dataset
- File: `synthetic_telco_churn.csv` (generated for this project, no external download required)

## Tech
- Python, Pandas, NumPy, scikit-learn

## How to Run
```bash
pip install -r requirements.txt
python churn_train.py
```

## Output
- Console metrics (Accuracy + classification report)
- `predictions.csv` with true vs predicted labels

## Notes
- The dataset includes features like Tenure, MonthlyCharges, Contract type, InternetService, etc.
- Churn signal is simulated so you can demo EDA and modeling.
