USE sales_accenture;

CREATE INDEX idx_sales_date_product ON sales(SalesDate, ProductID);
CREATE INDEX idx_sales_customer_date ON sales(CustomerID, SalesDate);