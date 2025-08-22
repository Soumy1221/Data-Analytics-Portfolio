# Sales Performance Dashboard

Interactive **Power BI** dashboard using a synthetic sales dataset.

## Files
- `sales_data.csv`: 5,000 transactions with OrderDate, ProductName, Region, Quantity, Sales, Profit
- `sales_queries.sql`: example SQL to use if you load into MySQL/Postgres/SQL Server first

## Build in Power BI
1. Load `sales_data.csv` into Power BI.
2. Create measures (examples):
   - **Total Sales** = SUM(Sales)
   - **Total Profit** = SUM(Profit)
   - **Profit Margin** = DIVIDE([Total Profit], [Total Sales])
3. Recommended visuals:
   - Line: Sales by Month
   - Bar: Sales by Region
   - Bar: Top Products by Sales
   - Card KPIs: Total Sales, Total Profit, Profit Margin
4. Add slicers for Region and ProductName.
5. (Optional) Instead of CSV, import via SQL using `sales_queries.sql`.

## Deliverables
- Export screenshots of the dashboard to use in your README and resume.
