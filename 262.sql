# Write your MySQL query statement below
select a.Day, round(ifnull(sum2/sum1, 0), 2) 'Cancellation Rate' from
	-- 总次数
	(select count(*) sum1, Request_at Day
	from Trips
	where Request_at between '2013-10-01' and '2013-10-03'
	and Client_Id in (select Users_Id from Users where Banned = 'No')
	group by Request_at) a
left join
	-- 取消次数
	(select count(*) sum2, Request_at Day
	from Trips
	where Request_at between '2013-10-01' and '2013-10-03'
	and Status in ('cancelled_by_driver', 'cancelled_by_client')
	and Client_Id in (select Users_Id from Users where Banned = 'No')
	group by Request_at
  ) b
on a.Day = b.Day
