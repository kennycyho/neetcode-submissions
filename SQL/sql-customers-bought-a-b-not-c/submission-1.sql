-- Write your query below
select c.customer_id, c.customer_name
from customers c where c.customer_id in
(select distinct c.customer_id from customers c join orders o on c.customer_id = o.customer_id where product_name='A'
intersect
select distinct c.customer_id from customers c join orders o on c.customer_id = o.customer_id where product_name='B'
except
select distinct c.customer_id from customers c join orders o on c.customer_id = o.customer_id where product_name='C')
order by customer_name;