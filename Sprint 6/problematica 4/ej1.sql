SELECT sucursal.branch_name AS "Nombre_de_la_sucursal", COUNT (customer_id) AS "Total_por_sucursal" 
FROM cliente JOIN sucursal ON cliente.branch_id = sucursal.branch_id 
GROUP BY sucursal.branch_name 
ORDER BY Total_por_sucursal DESC