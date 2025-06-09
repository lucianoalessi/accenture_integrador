USE sales_accenture;

DROP PROCEDURE IF EXISTS get_employees_by_age_range;

CREATE PROCEDURE get_employees_by_age_range(IN min_age INT, IN max_age INT)
BEGIN
    SELECT
        EmployeeID,
        CONCAT(FirstName, ' ', LastName) AS EmployeeName,
        calculate_age(BirthDate) AS Age,
        Gender,
        HireDate
    FROM employees
    WHERE calculate_age(BirthDate) BETWEEN min_age AND max_age
    ORDER BY Age;
END;

