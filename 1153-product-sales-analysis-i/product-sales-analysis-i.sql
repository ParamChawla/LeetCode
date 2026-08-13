# Write your MySQL query statement below
Select prd.product_name,sls.year,sls.price
From Product prd
INNER JOIN Sales sls
ON prd.product_id = sls.product_id;