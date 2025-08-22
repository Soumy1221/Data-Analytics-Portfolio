# HR Analytics Dashboard

Interactive **Power BI** dashboard for HR KPIs using a synthetic dataset (`hr_data.csv`).

## KPIs
- Employee Count
- Attrition %
- Average Monthly Income
- Average Years at Company

## Build Steps
1. Load `hr_data.csv` into Power BI.
2. Create measures:
   - **Employee Count** = DISTINCTCOUNT(EmployeeID)
   - **Attrition Count** = CALCULATE(COUNTROWS(hr_data), hr_data[Attrition] = "Yes")
   - **Attrition %** = DIVIDE([Attrition Count], [Employee Count])
   - **Avg Monthly Income** = AVERAGE(hr_data[MonthlyIncome])
   - **Avg Years at Company** = AVERAGE(hr_data[YearsAtCompany])
3. Visuals to add:
   - Bar: Attrition by Department
   - Bar: Attrition by JobRole
   - Line: Hiring Trend over time (by HiringDate)
   - Cards: KPIs above
4. Add slicers for Gender, Education, Department.

## Deliverables
- Export dashboard screenshots and add to this README.
