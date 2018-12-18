# Write your MySQL query statement below
select * from
    (select id-1 id, student from seat where id&1=0 -- 偶数id改为id-1
    union
    select id+1 id, student from seat where id&1=1 and id+1 <= (select count(*) from seat) -- 奇数id改为id+1
    union
    select id id, student from seat where id&1=1 and id+1 > (select count(*) from seat) )a
order by id
