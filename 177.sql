CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT

BEGIN
  SET N = N - 1; -- 偏移量，第二大时偏移量为1
  RETURN (
      # Write your MySQL query statement below.
      select ifnull(
        (select distinct Salary from Employee
        order by Salary desc
        limit 1 offset N), null) -- 增加偏移量
         );
END
