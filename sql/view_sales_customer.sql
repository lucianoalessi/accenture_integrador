USE sales_accenture;

CREATE OR REPLACE VIEW vista_ventas_clientes AS
SELECT
    s.SalesID,
    s.TotalPrice,
    s.SalesDate,
    c.FirstName,
    c.LastName
FROM sales s
JOIN customers c ON s.CustomerID = c.CustomerID;