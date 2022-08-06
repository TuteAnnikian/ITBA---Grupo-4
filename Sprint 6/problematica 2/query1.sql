CREATE VIEW Vista1
AS
SELECT
customer_id, 
branch_id, 
customer_name,
customer_surname,customer_DNI,
(strftime('%Y', 'now') - strftime('%Y', dob)) - (strftime('%m-%d', 'now') < strftime('%m-%d', dob))AS edad 
FROM cliente;

SELECT * FROM Vista1 
WHERE (edad > 40) 
ORDER BY customer_DNI ASC ;

SELECT * FROM Vista1
WHERE customer_name = "Anne" OR customer_name = "Tyler"
ORDER BY edad ASC
--------------------------------------------------------------
INSERT INTO cliente (customer_name, customer_surname, customer_DNI, branch_id, dob)
VALUES ("Lois", "Stout", "47730534", 80, "1984-07-07"),
("Hall", "Mcconnell", "52055464", 45, "1968-04-30"),
("Hilel", "Mclean", "43625213", 77, "1993-03-28"),
("Jin", "Cooley", "21207908", 96, "1959-08-24"),
("Gabriel", "Harmon", "57063950", 27, "1976-04-01");

--select * from cliente where customer_id > 500--

UPDATE cliente SET branch_id = 10 WHERE customer_id > 500 and customer_id <= 505;
--------------------------------------------------------------

DELETE FROM cliente where customer_name = "Noel" and customer_name = "David" 

--------------------------------------------------------------
SELECT loan_id, loan_type FROM prestamo ORDER BY loan_total DESC limit 1
---------------------------------------------------------------
