USE sales_accenture;

-- 1. Vista: Resumen de ventas por empleado y mes
CREATE OR REPLACE VIEW sales_by_employee_month AS
SELECT
    e.EmployeeID,
    CONCAT(e.FirstName, ' ', e.LastName) as EmployeeName,
    YEAR(s.SalesDate) as Year,
    MONTH(s.SalesDate) as Month,
    COUNT(*) as TotalTransactions,
    SUM(s.Quantity) as TotalQuantity,
    SUM(s.TotalPrice) as TotalSales
FROM sales s
JOIN employees e ON s.SalesPersonID = e.EmployeeID
GROUP BY e.EmployeeID, EmployeeName, YEAR(s.SalesDate), MONTH(s.SalesDate)
ORDER BY Year, Month, TotalSales DESC;