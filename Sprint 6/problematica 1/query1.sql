CREATE TABLE "tipo_cliente" (
    "tipo_cliente_id" INTEGER NOT NULL,
    "tipo_cliente_nombre" TEXT NOT NULL,
    PRIMARY KEY ("tipo_cliente_id" AUTOINCREMENT)
)

CREATE TABLE "tipo_cuenta" (
    "tipo_cuenta_id" INTEGER NOT NULL,
    "tipo_cuenta_nombre" TEXT NOT NULL,
    PRIMARY KEY ("tipo_cuenta_id" AUTOINCREMENT)
)

CREATE TABLE "marca_tarjeta" (
    "marca_id" INTEGER NOT NULL,
    "marca_nombre" TEXT NOT NULL,
    PRIMARY KEY ("marca_id" AUTOINCREMENT)
)

CREATE TABLE "direccion" (
    "direccion_id" INTEGER NOT NULL, 
    "calle" TEXT,
    "numero" INTEGER,
    "ciudad" TEXT,
    "provincia" TEXT,
    "pais" TEXT, 
    "sucursal_id" INTEGER,
    "cliente_id" INTEGER,
    "empleado_id" INTEGER,

    FOREIGN KEY ("sucursal_id") REFERENCES sucursal(branch_id)
    UNIQUE ("sucursal_id")

    FOREIGN KEY ("cliente_id") REFERENCES cliente(customer_id)

    FOREIGN KEY ("empleado_id") REFERENCES empleado(employee_id)

    PRIMARY KEY ("direccion_id" AUTOINCREMENT)
)

CREATE TABLE "tarjeta" (
    "numero" INTEGER (20) NOT NULL,
    "CVV" INTEGER (3) NOT NULL,
    "fecha_otorgamiento" TEXT NOT NULL,
    "fecha_expiracion" TEXT NOT NULL,
    "credito_debito" TEXT NOT NULL,
    "marca_id" INTEGER NOT NULL, 
    "cliente_id" INTEGER NOT NULL,
    FOREIGN KEY ("marca_id") REFERENCES marca_tarjeta(marca_id)
    FOREIGN KEY ("cliente_id") REFERENCES cliente(customer_id)
    UNIQUE("numero"),
    PRIMARY KEY ("numero")
)

ALTER TABLE cliente 
ADD COLUMN direccion_id INTEGER REFERENCES direccion(direccion_id)

ALTER TABLE empleado 
ADD COLUMN direccion_id INTEGER REFERENCES direccion(direccion_id)

ALTER TABLE cuenta
ADD COLUMN tipo_cuenta_id INTEGER REFERENCES tipo_cuenta(tipo_cuenta_id)

