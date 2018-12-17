# Write your MySQL query statement below
delete from Person
where Id not in
	-- 不能先select出同一表中的某些值，再update这个表
	-- 查询的时候增加一层中间表，就可以避免该错误
	(select Id from
		(select min(Id) Id
		from Person
		group by Email) a)
