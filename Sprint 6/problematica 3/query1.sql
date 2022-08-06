SELECT * FROM cuenta WHERE balance < 0;

SELECT customer_name,customer_surname,edad FROM Vista1 
WHERE customer_surname LIKE'%z%' ;

SELECT customer_name,customer_surname,edad, sucursal.branch_name AS 'sucursal' 
FROM Vista1 JOIN sucursal ON Vista1.branch_id = sucursal.branch_id 
WHERE customer_name = 'Brendan';

SELECT * FROM prestamo 
WHERE loan_type = 'PRENDARIO' and loan_total > 80000.00;

SELECT * FROM prestamo 
WHERE loan_total > (SELECT AVG(loan_total) FROM prestamo);

SELECT COUNT (customer_id) FROM Vista1 WHERE edad > 50;

SELECT * FROM cuenta WHERE balance > 8000 
ORDER BY balance DESC LIMIT 5;

SELECT * FROM prestamo 
WHERE strftime('%m', loan_date)='04' 
OR strftime('%m', loan_date)='06' 
OR strftime('%m', loan_date)='08'
ORDER BY loan_total;

SELECT loan_type, SUM(loan_total)AS 'loan_total_accu' FROM prestamo GROUP BY loan_type;



