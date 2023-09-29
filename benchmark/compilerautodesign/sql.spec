SQL syntax:

Retrieving data from a table:



SELECT column1, column2, ...
FROM table_name;
Example:

Retrieve all columns from the employee table:




SELECT * FROM employee;
Inserting data into a table:



INSERT INTO table_name ( column1, column2, ...)
VALUES ( value1, value2, ...);
Example: Insert a new record into the employee table:




INSERT INTO employee (id, name, age, gender) VALUES (1, 'John Doe', 35, 'Male');
Updating data in a table:



UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
Example: Update the age of the employee with ID=1:




UPDATE employee SET age = 40 WHERE id = 1;
Deleting data from a table:



DELETE FROM table_name WHERE condition;
Example: Delete the record of the employee with ID=1:




DELETE FROM employee WHERE id = 1;
Creating a new table:



CREATE TABLE table_name (
column1 datatype1,
column2 datatype2,
...
);
Example: Create a new table called employee with columns id, name, age, gender:




CREATE TABLE employee (
id INT,
name VARCHAR(50),
age INT,
gender VARCHAR(10)
);