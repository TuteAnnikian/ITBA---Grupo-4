import json
from clases import *
from htmlwriter import create_report
import sys

try:
    path = sys.argv[1]
except:
    if (len(sys.argv)) < 2:
        path = input("Ingrese path: ") #\eventos_black.json

try:
    with open(path, "r") as tps_file:
        evento = json.load(tps_file)
except:
    print(f"Error al abrir el archivo en: '\{path}'")
    exit()

# recorriendo el diccionario con un for (esto recorreria "cada cliente"), luego accedemos a los valores que nos interesan
#mediante las keys/claves (diccionario["clave"] => nos da el valor)
#luego recorremos los elementos dentro de la clave "transacciones"
#en este caso hay un solo cliente

numero_cli = evento["numero"]
nombre_cli = evento["nombre"]
apellido_cli = evento["apellido"]
dni_cli = evento["dni"]
dicc_direccion = evento["direccion"] # es un diccionario
tipo_cli = evento["tipo"]
transacciones = evento["transacciones"] # es una lista de diccionarios

if tipo_cli == "CLASSIC":
    print("Creando cliente classic...")
    cliente_actual = Classic(nombre_cli,apellido_cli, numero_cli, dni_cli,dicc_direccion)
elif tipo_cli == "GOLD":
    print("Creando cliente gold...")
    cliente_actual = Gold(nombre_cli,apellido_cli, numero_cli, dni_cli,dicc_direccion)
elif tipo_cli == "BLACK":
    print("Creando cliente black...")
    cliente_actual = Black(nombre_cli,apellido_cli, numero_cli, dni_cli,dicc_direccion)
else:
    print("No se reconoce el tipo de cliente")

direc = dicc_direccion["calle"]," ", dicc_direccion["numero"],", ",dicc_direccion["ciudad"],", ",dicc_direccion["provincia"],", ",dicc_direccion["pais"]
str_direc=""
for item in direc:
    str_direc=str_direc + item
print (str_direc)

cliente_info = f"""
<table id="info_cli">   
  <tr>
    <th>No. Cliente</th>
    <th>Nombre</th>
    <th>DNI</th>
    <th>Dirección</th>
  </tr>
  <tr>
    <td>{numero_cli}</td>
    <td>{nombre_cli} {apellido_cli}</td>
    <td>{dni_cli}</td>
    <td>{str_direc}</td>
  </tr>
</table>"""

ops= "" #string vacia donde vamos a poner las transacciones

for operacion in transacciones:
    numero = operacion["numero"]
    fecha = operacion["fecha"]
    tipo = operacion["tipo"]
    estado = operacion["estado"]
    monto = operacion["monto"]

    print(operacion["numero"],operacion["tipo"])

    if operacion["estado"] == "ACEPTADA":
        print("aceptada ok ")
        rechazo = " - "
    elif operacion["estado"] == "RECHAZADA":
        print("rechazada")
        operacion_actual = Transaccion(operacion["estado"], operacion["tipo"], operacion["cuentaNumero"],operacion["cupoDiarioRestante"],operacion["monto"],operacion["fecha"],operacion["numero"],operacion["saldoEnCuenta"],operacion["totalTarjetasDeCreditoActualmente"],operacion["totalChequerasActualmente"])
        if operacion["tipo"] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
            print(cliente_actual.retiro_efectivo_cajero_automatico(operacion_actual))
            rechazo = cliente_actual.retiro_efectivo_cajero_automatico(operacion_actual)

        elif operacion["tipo"] == "ALTA_TARJETA_CREDITO":
            print(cliente_actual.alta_tarjeta_credito(operacion_actual))
            rechazo = cliente_actual.alta_tarjeta_credito(operacion_actual)

        elif operacion["tipo"] == "ALTA_CHEQUERA":
            print(cliente_actual.alta_chequera(operacion_actual))
            rechazo = cliente_actual.alta_chequera(operacion_actual)

        elif operacion["tipo"] == "COMPRA_DOLAR":
            print(cliente_actual.comprar_dolar(operacion_actual))
            rechazo = cliente_actual.comprar_dolar(operacion_actual)

        elif operacion["tipo"] == "TRANSFERENCIA_ENVIADA":
            print(cliente_actual.transferencia_enviada(operacion_actual))
            rechazo = cliente_actual.transferencia_enviada(operacion_actual)

        elif operacion["tipo"] == "TRANSFERENCIA_RECIBIDA":
            print(cliente_actual.transferencia_recibida(operacion_actual))
            rechazo = cliente_actual.transferencia_recibida(operacion_actual)

# para cada transacción la fecha , el tipo de operación, el estado, el monto y razón por la
#cual se rechazó (vacío en caso de ser aceptada).

    #en esta variable guardamos cada una de las filas que generamos por transaccion
    op_report= f"""
    <tr>
        <td>{numero}</td>
        <td>{fecha}</td>
        <td>{tipo}</td>
        <td>{estado}</td>
        <td>{monto}</td>
        <td>{rechazo}</td>
    </tr>
    """
    ops = ops + op_report
#*************************************************************************************************

transac_info= f"""
<table>   
  <tr>
    <th>No. Transaccion</th>
    <th>Fecha</th>
    <th>Tipo de operacion</th>
    <th>Estado</th>
    <th>Monto</th>
    <th>Razon rechazo</th>
  </tr>
  {ops}
</table>"""

fname = f"reporte_{dni_cli}_{apellido_cli.lower()}{nombre_cli.lower()}" #el nombre del archivo .html que contiene el reporte

create_report(transac_info,cliente_info,fname)




