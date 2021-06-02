---1. INNER JOIN
select d.departmentName, d.sub-class, s.studentName, s.grade
from department d
inner join Students s
on d.departmentID = s.departmentID

-- Description: inner joın returns only matching records, here we are getting only students with valid matching departmentID. DepartmentID is a connecting field(column) that helps to build the relationship between this table.

-- 2. FULL OUTER JOIN
select d.departmentName, d.sub-class, s.studentName, s.grade
from department d
FULL OUTER JOIN Students s
on d.departmentID = s.departmentID

-- Description: OUTER JOIN returns all matching and not matching records from both tables.
-- when we use outer join we will get the all records from Students and all records from Department table, matching records using departmentID will have valid values from both tables. Students with no valid departmentIDs are also expected to be listed but those records will have NULL values for departmentName, sub-class (also other fields from Department table). Records from departments that does not have students also expected to be listed and have NULL values for not matching records for columns from Students table.

-- 3. LEFT JOIN
select d.departmentName, d.sub-class, s.studentName, s.grade
from department d
LEFT JOIN Students s
on d.departmentID = s.departmentID

-- Description: LEFT JOIN returns all records from left table (department). All records from Department table expected to be listed, matching records (using departmenID) expected to have values from Students table, not matching records expected to have NULL values for the field from Students table

-- 4. RIGHT JOIN
select d.departmentName, d.sub-class, s.studentName, s.grade
from department d
RIGHT JOIN Students s
on d.departmentID = s.departmentID

-- Description: RIGHT JOIN returns all records from right table (students). Students with no valid departmentIDs are also expected to be listed but those records will have NULL values for departmentName, sub-class (also other fields from Department table)