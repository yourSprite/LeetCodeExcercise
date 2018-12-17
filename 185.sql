# Write your MySQL query statement below
select cc.Name Department, aa.Name Employee, aa.Salary
from Employee aa
right join
		(-- 取出每个部门前三条数据
    select distinct a.Salary,a.DepartmentId
    from Employee a
    where (select count(distinct Salary) from Employee where DepartmentId = a.DepartmentId and a.Salary < Salary) < 3
    ) bb
on aa.Salary = bb.Salary
and aa.DepartmentId = bb.DepartmentId
left join Department cc
on aa.DepartmentId = cc.Id
where cc.Name is not null
order by cc.Id, aa.Salary desc
