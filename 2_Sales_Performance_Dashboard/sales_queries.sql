-- Create table example
-- CREATE TABLE sales_data (
--   OrderDate DATE,
--   ProductName VARCHAR(100),
--   Region VARCHAR(50),
--   Quantity INT,
--   UnitPrice DECIMAL(10,2),
--   Sales DECIMAL(12,2),
--   Profit DECIMAL(12,2)
-- );

-- Total Sales by Month
SELECT DATE_FORMAT(OrderDate, '%Y-%m') AS Month, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY DATE_FORMAT(OrderDate, '%Y-%m')
ORDER BY Month;

-- Top 5 Products by Sales
SELECT ProductName, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY ProductName
ORDER BY Total_Sales DESC
LIMIT 5;

-- Sales by Region
SELECT Region, SUM(Sales) AS Total_Sales, SUM(Profit) AS Total_Profit
FROM sales_data
GROUP BY Region;

-- Profit Margin by Product
SELECT ProductName, SUM(Profit)/NULLIF(SUM(Sales),0) AS Profit_Margin
FROM sales_data
GROUP BY ProductName
ORDER BY Profit_Margin DESC;
