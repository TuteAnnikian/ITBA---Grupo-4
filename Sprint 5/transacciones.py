import json


with open("eventos_black.json", "r") as black:
    evento_black = json.load(black)
    # print (evento_black)

with open("eventos_classic.json", "r") as classic:
    evento_classic = json.load(classic)
    # print (evento_classic)
    
with open("eventos_gold.json", "r") as gold:
    evento_gold = json.load(gold)
    # print (evento_gold)
    

# ***** Clase transaccion: estado, tipo, numero de cuenta, cupo diario restante, monto, fecha, numero, saldo en cuenta, total de tarjetas de credito que tiene actualmente y total de chequeras que tiene actualmente ***** #
class Transaccion:
    def __init__(self, estado, tipo, cuentaNumero, cupoDiarioRestante, monto, fecha, numero, saldoEnCuenta, totalTarjetasDeCreditoActualmente, totalChequerasActualmente):
        self.estado = estado
        self.tipo = tipo
        self.cuentaNumero = cuentaNumero
        self.cupoDiarioRestante = cupoDiarioRestante
        self.monto = monto
        self.fecha = fecha
        self.numero = numero
        self.saldoEnCuenta = saldoEnCuenta
        self.totalTarjetasDeCreditoActualmente = totalTarjetasDeCreditoActualmente
        self.totalChequerasActualmente = totalChequerasActualmente
# *********************************** Fin de la clase *********************************** #




# ***** Clase cliente: numero, nombre, apellido, dni, tipo y direccion {calle, numero, ciudad, provincia } ***** #
class Cliente(object):
    def __init__(self, numero, nombre, apellido, dni, tipo, direccion, transacciones):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.tipo = tipo
        self.direccion = direccion
        self.transacciones = transacciones
            # "calle": None,
            # "numero": None,
            # "ciudad": None,
            # "provincia": None,
            # "pais": None
        # }
        
    
# *********************************** Fin de la clase *********************************** #



# *****Clase cliente Classic: chequera (no), tarjeta de credito (no) y comprar dolares (no) ***** #
class Classic(Cliente):
    def __init__(self, numero, nombre, apellido, dni, direccion):
        pass
    def puede_crear_chequera(self):
        return False
    def puede_crear_tarjeta_credito(self):
        return False
    def puede_comprar_dolar(self):
        return False
# *********************************** Fin de la clase *********************************** #



# ***** Clase cliente Gold: chequera (1), tarjeta de credito (1) y comprar dolares (si) ***** #
class Gold(Cliente):
    def __init__(self, numero, nombre, apellido, dni, direccion):
        pass
    def puede_crear_chequera(self):
        return True
    def puede_crear_tarjeta_credito(self):
        return True
    def puede_comprar_dolar(self):
        return True
# *********************************** Fin de la clase *********************************** #



# ***** Clase cliente Black: chequera (2), tarjeta de credito (5) y comprar dolares (si) ***** #
class Black(Cliente):
    def __init__(self, numero, nombre, apellido, dni, direccion):
        pass
    def puede_crear_chequera(self):
        return True
    def puede_crear_tarjeta_credito(self):
        return True
    def puede_comprar_dolar(self):
        return True
# *********************************** Fin de la clase *********************************** #





# ***** Evento Classic ***** #
for cliente in evento_classic:
    cliente1 = Cliente(evento_classic["numero"], evento_classic["nombre"], evento_classic["apellido"], evento_classic["dni"],evento_classic["tipo"], evento_classic["direccion"], evento_classic["transacciones"])
    # ***** Si es una cuenta classic,  ***** #
if cliente1.tipo == "CLASSIC":
    print("----------------------")
    print("Cliente:", cliente1.nombre, cliente1.apellido + "." + "\nTipo de cuenta:",cliente1.tipo + ".") 
    print("----------------------")
    for operaciones in cliente1.transacciones:
        transaccion = Transaccion(operaciones["estado"], operaciones["tipo"], operaciones["cuentaNumero"], operaciones["cupoDiarioRestante"], operaciones["monto"], operaciones["fecha"], operaciones["numero"], operaciones["saldoEnCuenta"], operaciones["totalTarjetasDeCreditoActualmente"], operaciones["totalChequerasActualmente"])
        print("Transacción Nº:", transaccion.numero)
        
        if transaccion.estado == "ACEPTADA":                
            print("Todo OK")
        else:
            if transaccion.tipo == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                if transaccion.monto>transaccion.saldoEnCuenta:
                    print("El saldo en cuenta es insuficiente para realizar la operación.")
                elif transaccion.monto>transaccion.cupoDiarioRestante:
                    print("El cupo diario restante para retirar efectivo en cajero automático es insuficiente para realizar la operacion.")
                else:
                    print("Error.")
            elif transaccion.tipo == "ALTA_TARJETA_CREDITO":
                print("Su tipo de cuenta no le permite dar de alta tarjetas de crédito.")
            elif transaccion.tipo == "ALTA_CHEQUERA":
                print("Su tipo de cuenta no le permite dar de alta chequeras.")
            elif transaccion.tipo == "COMPRA_DOLAR":
                print("Su tipo de cuenta no le permite comprar dólares.")
            elif transaccion.tipo == "TRANSFERENCIA_ENVIADA":
                if (int(transaccion.monto)*1.01)>transaccion.saldoEnCuenta:
                    print("El saldo en cuenta es insuficiente para realizar la operación. Debe tener en cuenta la comisión del 1 %.")
                else:
                    print("Error.")
            elif transaccion.tipo == "TRANSFERENCIA_RECIBIDA":
                if transaccion.monto>150000:
                    print("Debe pedir autorización al banco para recibir transferencias cuyos importes superen los $150.000,00.")
                else:
                    print("Error.")
# *********************************** Fin del ciclo for *********************************** #





# ***** Evento Gold ***** #                    
for cliente in evento_gold:
    cliente1 = Cliente(evento_gold["numero"], evento_gold["nombre"], evento_gold["apellido"], evento_gold["dni"],evento_gold["tipo"], evento_gold["direccion"], evento_gold["transacciones"])
if cliente1.tipo == "GOLD":
    print("----------------------")
    print("Cliente:", cliente1.nombre, cliente1.apellido + "." + "\nTipo de cuenta:",cliente1.tipo + ".") 
    print("----------------------")
    for operaciones in cliente1.transacciones:
        transaccion = Transaccion(operaciones["estado"], operaciones["tipo"], operaciones["cuentaNumero"], operaciones["cupoDiarioRestante"], operaciones["monto"], operaciones["fecha"], operaciones["numero"], operaciones["saldoEnCuenta"], operaciones["totalTarjetasDeCreditoActualmente"], operaciones["totalChequerasActualmente"])
        print("Transacción Nº:", transaccion.numero)
        if transaccion.estado == "ACEPTADA":                
            print("Todo OK")
        else:
            if transaccion.tipo == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                if transaccion.monto>(int(transaccion.saldoEnCuenta)+10000):
                    print("El saldo en cuenta es insuficiente para realizar la operación.")
                elif transaccion.monto>transaccion.cupoDiarioRestante:
                    print("El cupo diario restante para retirar efectivo en cajero automático es insuficiente para realizar la operacion.")
                else:
                    print("Error. (Puede ser que sea por haber tenido en cuenta el descubierto).")
            elif transaccion.tipo == "ALTA_TARJETA_CREDITO":
                if transaccion.totalTarjetasDeCreditoActualmente == 1:
                    print("Su tipo de cuenta no le permite dar de alta más de 1 tarjeta de crédito.")
                else:
                    print("Error.")
            elif transaccion.tipo == "ALTA_CHEQUERA":
                if transaccion.totalChequerasActualmente == 1:
                    print("Su tipo de cuenta no le permite dar de alta más de 1 chequera.")
                else:
                    print("Error.")
            elif transaccion.tipo == "COMPRA_DOLAR":
                if transaccion.monto>(transaccion.saldoEnCuenta):
                    print("El saldo en cuenta es insuficiente para realizar la operación.")
                else:
                    print("Error. (Puede ser que sea por haber tenido en cuenta el descubierto).")
            elif transaccion.tipo == "TRANSFERENCIA_ENVIADA":
                if (transaccion.monto*1.005)>(transaccion.saldoEnCuenta+10000):
                    print("El saldo en cuenta es insuficiente para realizar la operación. Debe tener en cuenta la comisión del 0,5 %.")
                else:
                    print("Error. (Puede ser que sea por haber tenido en cuenta el descubierto).")
            elif transaccion.tipo == "TRANSFERENCIA_RECIBIDA":
                if transaccion.monto>500000:
                    print("Debe pedir autorización al banco para recibir transferencias cuyos importes superen los $500.000,00.")
                else:
                    print("Error.")                    





# ***** Evento Black ***** #
for cliente in evento_black:
    cliente1 = Cliente(evento_black["numero"], evento_black["nombre"], evento_black["apellido"], evento_black["dni"],evento_black["tipo"], evento_black["direccion"], evento_black["transacciones"])
if cliente1.tipo == "BLACK":
    print("----------------------")
    print("Cliente:", cliente1.nombre, cliente1.apellido + "." + "\nTipo de cuenta:",cliente1.tipo +".") 
    print("----------------------")
    for operaciones in cliente1.transacciones:
        transaccion = Transaccion(operaciones["estado"], operaciones["tipo"], operaciones["cuentaNumero"], operaciones["cupoDiarioRestante"], operaciones["monto"], operaciones["fecha"], operaciones["numero"], operaciones["saldoEnCuenta"], operaciones["totalTarjetasDeCreditoActualmente"], operaciones["totalChequerasActualmente"])
        print("Transacción Nº:", transaccion.numero)
        if transaccion.estado == "ACEPTADA":                
            print("Todo OK")
        else:
            if transaccion.tipo == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
                if transaccion.monto>(int(transaccion.saldoEnCuenta)+10000):
                    print("El saldo en cuenta es insuficiente para realizar la operación.")
                elif transaccion.monto>transaccion.cupoDiarioRestante:
                    print("El cupo diario restastante para retirar efectivo en cajero automático es insuficiente para realizar la operacion.")
                else:
                    print("Error. (Puede ser que sea por haber tenido en cuenta el descubierto).")
            elif transaccion.tipo == "ALTA_TARJETA_CREDITO":
                if transaccion.totalTarjetasDeCreditoActualmente == 5:
                    print("Su tipo de cuenta no le permite dar de alta más de 5 tarjeta de crédito.")
                else:
                    print("Error.")
            elif transaccion.tipo == "ALTA_CHEQUERA":
                if transaccion.totalChequerasActualmente == 2:
                    print("Su tipo de cuenta no le permite dar de alta más de 2 chequeras.")
                else:
                    print("Error.")
            elif transaccion.tipo == "COMPRA_DOLAR":
                if transaccion.monto>(transaccion.saldoEnCuenta):
                    print("El saldo en cuenta es insuficiente para realizar la operación.")
                else:
                    print("Error. (Puede ser que sea por haber tenido en cuenta el descubierto).")
            elif transaccion.tipo == "TRANSFERENCIA_ENVIADA":
                if (transaccion.monto)>(transaccion.saldoEnCuenta+10000):
                    print("El saldo en cuenta es insuficiente para realizar la operación.")
                else:
                    print("Error. (Puede ser que sea por haber tenido en cuenta el descubierto).")
            elif transaccion.tipo == "TRANSFERENCIA_RECIBIDA":
                    print("Error.")
# *********************************** Fin del ciclo for *********************************** #                        