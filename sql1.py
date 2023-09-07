import sqlite3
con=sqlite3.connect("database.db")
print("connection established")
# con.execute("CREATE TABLE EMPLOYEE (EmployeeID int primary key, Ename varchar(20), DeptID int, Salary int, Dname varchar(20), Dlocation varchar(30))")
# con.execute("INSERT INTO EMPLOYEE VALUES (1001,'John',2,4000,'IT','New Delhi')")
# con.execute("INSERT INTO EMPLOYEE VALUES (1002,'Anna',1,3500,'HR','Mumbai')")
# con.execute("INSERT INTO EMPLOYEE VALUES (1003,'James',1,2500,'HR','Mumbai')")
# con.execute("INSERT INTO EMPLOYEE VALUES (1004,'David',2,5000,'IT','New Delhi')")
# con.execute("INSERT INTO EMPLOYEE VALUES (1005,'Mark',2,3000,'IT','New Delhi')")
# con.execute("INSERT INTO EMPLOYEE VALUES (1006,'Steve',3,4500,'FINANCE','Mumbai')")
# con.execute("INSERT INTO EMPLOYEE VALUES (1007,'Alice',3,3500,'FINANCE','Mumbai')")

# x=con.execute("update EMPLOYEE set Dname = 'Software' where EmployeeID = 1006")
x=con.execute("SELECT * FROM users")
for i in x:
    print(i)
con.commit()
con.close()