SELECT branch_name AS sucursal, COUNT(loan_id)AS cantidad_prestamos, AVG(loan_total)AS valor_promedio FROM prestamo 
JOIN cliente ON cliente.customer_id = prestamo.customer_id 
JOIN sucursal ON cliente.branch_id = sucursal.branch_id
GROUP BY sucursal.branch_name