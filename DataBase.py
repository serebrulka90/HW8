import sqlite3

conn = sqlite3.connect("Company.db")
cursor = conn.cursor()

cursor.execute(
    '''CREATE TABLE Employees
        (Id INTEGER PRIMARY KEY AUTOINCREMENT,
        FirstName TEXT,
        LastName TEXT,
        Email TEXT,
        Age INTEGER)'''
)

cursor.execute(
    '''CREATE TABLE Salaries
        (Id INTEGER PRIMARY KEY AUTOINCREMENT,
        EmployeeId INTEGER,
        GrossSalary FLOAT,
        NetSalary FLOAT,
        YearsInCompany INTEGER,
        FOREIGN KEY (EmployeeId) REFERENCES Employees(Id))'''
)

cursor.execute(
    '''CREATE TABLE Position
        (Id INTEGER PRIMARY KEY AUTOINCREMENT,
        EmployeeId INTEGER,
        Name TEXT,
        BestSkill TEXT,
        WorstSkill TEXT,
        FOREIGN KEY (EmployeeId) REFERENCES Employees(Id))'''
)

conn.commit()
