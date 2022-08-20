CREATE TABLE "auditoria_cuenta" (
"change_id" INTEGER NOT NULL,
"old_id" INTEGER, 
"new_id" INTEGER,
"old_balance" INTEGER,
"new_balance" INTEGER,
"old_iban" TEXT,
"new_iban" TEXT, 
"old_type" INTEGER,
"new_type" INTEGER,
"user_action" TEXT,
"created_at" TEXT,
PRIMARY KEY ("change_id" AUTOINCREMENT)
)

CREATE TRIGGER auditoria
AFTER UPDATE ON cuenta
BEGIN
INSERT INTO auditoria_cuenta (old_id, new_id, old_balance, new_balance, old_iban, new_iban, old_type, new_type, user_action, created_at)
VALUES (old.account_id), (new.account_id), (old.balance), (new.balance), (old.iban), (new.iban), (old.tipo_cuenta_id), (new.tipo_cuenta_id), ("Actualiza datos"), (DATETIME("now"));
END

UPDATE cuenta SET balance = balance - 100 WHERE account_id = 10;
UPDATE cuenta SET balance = (balance - 100) WHERE account_id = 11;
UPDATE cuenta SET balance = balance - 100 WHERE account_id = 12;
UPDATE cuenta SET balance = balance - 100 WHERE account_id = 13;
UPDATE cuenta SET balance = balance - 100 WHERE account_id = 14;

SELECT balance FROM cuenta WHERE account_id = 10;