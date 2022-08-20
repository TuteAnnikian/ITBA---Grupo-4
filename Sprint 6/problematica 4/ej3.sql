SELECT sucursal.branch_name AS nombre_sucursal,tarjeta.credito_debito AS tipo_tarjeta,COUNT(tarjeta.numero) AS cantidad_tarjetas FROM 
tarjeta JOIN cliente ON tarjeta.cliente_id = cliente.customer_id 
JOIN sucursal ON sucursal.branch_id = cliente.branch_id
GROUP BY sucursal.branch_id,tarjeta.credito_debito
