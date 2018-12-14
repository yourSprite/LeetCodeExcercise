# Write your MySQL query statement below
-- 查询员工工资大于经理工资Name
select Name Employee from (
    -- 查询员工工资与对应经理工资
    select a.Id, a.Name, a.Salary, b.Salary ManagerSalary
    from Employee a
    left join Employee b
    on a.ManagerId = b.Id) c
where Salary > ManagerSalary
and ManagerSalary is not null
