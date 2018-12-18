# Write your MySQL query statement below
select class from
    (select count(student) num, class from
        (select distinct student, class
        from courses) a
    group by class) b
where num >= 5
