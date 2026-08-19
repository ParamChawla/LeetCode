# Write your MySQL query statement below
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
Where salary<(select max(salary)from employee);