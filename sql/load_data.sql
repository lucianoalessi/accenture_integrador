-- 1. Crear la base de datos
DROP DATABASE IF EXIST sales_accenture;
CREATE DATABASE IF NOT EXISTS sales_accenture;
USE sales_accenture;


-- 2. Crear las tablas
DROP TABLE IF EXISTS categories;
CREATE TABLE categories(
    CategoryID INT PRIMARY KEY,
    CategoryName VARCHAR(45)
);

DROP TABLE IF EXISTS cities;
CREATE TABLE cities(
    CityID INT PRIMARY KEY,
    CityName VARCHAR(45),
    Zipcode VARCHAR(10),
    CountryID INT
);

DROP TABLE IF EXIST countries;
CREATE TABLE countries(
    CountryID INT PRIMARY KEY,
    CountryName VARCHAR(100),
    CountryCode VARCHAR(10)
);

DROP TABLE IF EXIST customers;
CREATE TABLE customers(
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(100),
    MiddleInitial CHAR(1),
    LastName VARCHAR(100),
    CityID INT,
    Address VARCHAR(255)
);

DROP TABLE IF EXIST employees;
CREATE TABLE employees(
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(100),
    MiddleInitial CHAR(1),
    LastName VARCHAR(100),
    BirthDate DATETIME,
    Gender CHAR(1),
    CityID INT,
    HireDate  DATETIME
);

DROP TABLE IF EXIST products;
CREATE TABLE products(
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(255),
    Price DECIMAL(10,2),
    Class VARCHAR(50),
    ModifyDate TIME,
    Resistant VARCHAR(50),
    IsAllergic VARCHAR(10),
    VitalityDays  INT
);

DROP TABLE IF EXIST sales;
CREATE TABLE sales(
    SalesID INT PRIMARY KEY,
    SalesPersonID INT,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    Discount DECIMAL(4,2),
    TotalPrice DECIMAL(10,2),
    SalesDate DATETIME,
    TransactionNumber VARCHAR(50)
);


-- 3. Cargar datos desde archivos CSV

LOAD DATA LOCAL INFILE 'C:\Users\lucia\Desktop\accenture_trabajo_integrador\data\categories.csv'
INTO TABLE categories
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

SHOW GLOBAL VARIABLES LIKE 'local_infile';
SHOW GLOBAL VARIABLES LIKE 'local_infile';

SHOW VARIABLES LIKE 'secure_file_priv';



LOAD DATA INFILE ''
INTO TABLE customers
FIELDS TERMINATED BY ','
LINES TERMINATE BY '\n'
IGNORE 1 ROWS;

LOAD DATA INFILE ''
INTO TABLE customers
FIELDS TERMINATED BY ','
LINES TERMINATE BY '\n'
IGNORE 1 ROWS;