INSERT INTO tipo_cliente(tipo_cliente_nombre)
VALUES ("Classic"),("Gold"),("Black")

INSERT INTO tipo_cuenta(tipo_cuenta_nombre) 
VALUES ("Caja de ahorro"),("Cuenta corriente"),("Cuenta en dolares")

INSERT INTO marca_tarjeta (marca_nombre)
VALUES ("Visa"), ("MasterCard"), ("Cabal"), ("American Express"), ("Maestro")

UPDATE empleado SET 
employee_hire_date = (select substr(employee_hire_date,7,4)  ||"-"||  substr(employee_hire_date,4,2) || "-"||  substr(employee_hire_date,1,2) 
from empleado where empleado.employee_id = empleado.employee_id);