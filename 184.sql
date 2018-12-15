# Write your MySQL query statement below
select c.`Name` Department,
       b.`Name` Employee,
       a.Salary
from (-- 取出每个部门最高工资
	select max(Salary) Salary,
			   DepartmentId
	from Employee
	group by DepartmentId) a
left join Employee b -- 得到对应员工姓名
on a.Salary = b.Salary
and a.DepartmentId = b.DepartmentId
left join Department c -- 得到对应的部门
on a.DepartmentId = c.Id
where c.`Name` is not null -- 筛选部门为空数据
