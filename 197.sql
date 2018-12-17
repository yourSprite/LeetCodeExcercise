# Write your MySQL query statement below
select a.Id
from Weather a
join Weather b
on datediff(a.RecordDate, b.RecordDate) = 1
and a.Temperature > b.Temperature
