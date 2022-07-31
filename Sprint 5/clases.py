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

class Cliente:
    def __init__(self,nombre,apellido,numero,dni,direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni
        self.direccion = direccion 


# *********************************** Fin de la clase *********************************** #

class Classic(Cliente):
    def __init__(self,nombre,apellido,numero,dni,direccion):
        super().__init__(nombre,apellido,numero,dni,direccion)

    max_retiro_diario = 10000
    comi_transf =  0.01 #el monto viene de otro lado
    aviso_transf = 150000 #No puede recibir transferencias mayores a $150.000 sin previo aviso

    def retiro_efectivo_cajero_automatico(self,transaccion):
        disponible = transaccion.saldoEnCuenta
        restante = transaccion.cupoDiarioRestante
        monto = transaccion.monto
        if disponible >= monto and monto <= restante:
            return True
        else:
            if monto > restante:
                return f"Se excedio el cupo diario de ${self.max_retiro_diario} para extracciones, cupo diario restante: ${transaccion.cupoDiarioRestante}"
            elif monto > disponible:
                return f"Saldo insuficiente, saldo actual: ${transaccion.saldoEnCuenta}"

    def transferencia_enviada(self,transaccion):
        disponible = transaccion.saldoEnCuenta
        monto = transaccion.monto
        if disponible >= (monto + monto*self.comi_transf):
            return True
        else:
            return f"Saldo insuficiente (total a descontar: ${(monto + monto*self.comi_transf)})"

    def transferencia_recibida(self,transaccion):
        monto = transaccion.monto
        if monto <= self.aviso_transf:
            return True
        else: 
            return "No puede recibir transferencias mayores a $150.000 sin previo aviso."

    def alta_tarjeta_credito(self,transaccion):
        return "Su tipo de cuenta no permite tarjeta de credito"

    def alta_chequera(self,transaccion):
        return "Su tipo de cuenta no permite chequeras"
        
    def comprar_dolar(self,transaccion):
        return "Su tipo de cuenta no permite comprar dólares"
    
    
# *********************************** Fin de la clase *********************************** #


class Gold(Classic):
    def __init__(self,nombre,apellido,numero,dni,direccion):
        super().__init__(nombre,apellido,numero,dni,direccion)


    max_retiro_diario = 20000
    comi_transf =  0.005 
    aviso_transf = 500000 
    descubierto = 10000
    max_credito = 1
    max_chequera = 1 

    def retiro_efectivo_cajero_automatico(self,transaccion):
        disponible = (int(transaccion.saldoEnCuenta) +10000)
        restante = transaccion.cupoDiarioRestante
        monto = transaccion.monto
        if disponible >= monto and monto <= restante:
            return True
        else:
            if monto > restante:
                return f"Se excedio el cupo diario de ${self.max_retiro_diario} para extracciones, cupo diario restante: ${transaccion.cupoDiarioRestante}"
            elif monto > disponible:
                return f"Saldo insuficiente, saldo actual: ${transaccion.saldoEnCuenta}"


    def alta_tarjeta_credito(self,transaccion):
        if transaccion.totalTarjetasDeCreditoActualmente < self.max_credito: 
            return True
        else:
            return f"Se excede el maximo numero ({self.max_credito}) de tarjetas de credito para este tipo de cuenta"

    def alta_chequera(self,transaccion):
        if transaccion.totalChequerasActualmente < self.max_chequera: 
            return True
        else:
            return f"Se excede el maximo numero ({self.max_chequera}) de chequeras para este tipo de cuenta"

    def comprar_dolar(self,transaccion):
        if transaccion.monto <= transaccion.saldoEnCuenta:
            return True
        else:
            return f"Saldo insuficiente, su saldo es: ${transaccion.saldoEnCuenta}"
    
    def transferencia_enviada(self,transaccion):
        disponible = (int(transaccion.saldoEnCuenta) +10000)
        monto = transaccion.monto
        if disponible >= (monto + monto*self.comi_transf):
            return True
        else:
            return f"Saldo insuficiente (total a descontar: ${(monto + monto*self.comi_transf)})"

    def transferencia_recibida(self,transaccion):
        monto = transaccion.monto
        if monto <= self.aviso_transf:
            return True
        else: 
            return "No puede recibir transferencias mayores a $500.000 sin previo aviso."


# *********************************** Fin de la clase *********************************** #

class Black(Gold):
    def __init__(self,nombre,apellido,numero,dni,direccion):
        super().__init__(nombre,apellido,numero,dni,direccion)

    max_retiro_diario = 100000
    comi_transf =  0
    aviso_transf = 500000 
    descubierto = 10000
    max_credito = 5
    max_chequera = 2 

    # def retiro_efectivo_cajero_automatico(self,transaccion):
    #     disponible = (int(transaccion.saldoEnCuenta) +10000)
    #     restante = transaccion.cupoDiarioRestante
    #     monto = transaccion.monto
    #     if disponible >= monto and monto <= restante:
    #         return True
    #     else:
    #         if monto > restante:
    #             return f"Se excedio el cupo diario de ${self.max_retiro_diario} para extracciones, cupo diario restante: ${transaccion.cupoDiarioRestante}"
    #         elif monto > disponible:
    #             return f"Saldo insuficiente, saldo actual: {transaccion.saldoEnCuenta}"

    # def alta_tarjeta_credito(self,transaccion):
    #     if transaccion.totalTarjetasDeCreditoActualmente < self.max_credito: 
    #         return True
    #     else:
    #         return f"Se excede el maximo numero ({self.max_credito}) de tarjetas de credito para este tipo de cuenta"

    # def alta_chequera(self,transaccion):
    #     if transaccion.totalChequerasActualmente < self.max_chequera: 
    #         return True
    #     else:
    #         return f"Se excede el maximo numero ({self.max_chequera}) de chequeras para este tipo de cuenta"

    # def comprar_dolar(self,transaccion):
    #     if transaccion.monto <= transaccion.saldoEnCuenta:
    #         return True
    #     else:
    #         return f"Saldo insuficiente, su saldo es: {transaccion.saldoEnCuenta}"
    
    # def transferencia_enviada(self,transaccion):
    #     disponible = (int(transaccion.saldoEnCuenta) +10000)
    #     monto = transaccion.monto
    #     if disponible >= (monto + monto*self.comi_transf):
    #         return True
    #     else:
    #         return f"Saldo insuficiente (monto+comision: {(monto + monto*self.comi_transf)})"


    def transferencia_recibida(self,transaccion):
        return True

# *********************************** Fin de la clase *********************************** #

