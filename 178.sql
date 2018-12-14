# Write your MySQL query statement below
/*
1、取出不重复的数据并进行排序
2、对1中数据进行排序
3、用原表中的表left join排序结果，并进行输出
*/
-- 3、用原表中的表left join排序结果，并进行输出
select Scores.Score, cast(Rank as signed) Rank
from Scores
left join (
	-- 2、对1中数据进行排序
	select a.Score,(@i:=@i+1) Rank from (
		-- 1、取出不重复的数据并进行排序
		select distinct Score
		from Scores
		order by Score desc) a,(select @i:=0) as it) Rank
on Scores.Score = Rank.Score
order by Rank
