# Write your MySQL query statement below
select
     -- 为空返回null（只有一条记录）
     ifnull (
    (select distinct Salary
     from Employee
     order by Salary desc
     -- offset偏移量
     limit 1 offset 1),
     null) as SecondHighestSalary
