# PASO 1: Control de parámetros - ¿Que pasa si no me mandan todos los parametor obligatorios?
# PASO 2: Validación de parametros - ¿Que pasa si en los lugares donde tiene que estar los parametros hay otra cosa?
# PASO 3: Filtrar por DNI
# PASO 4: Filtrar por TIPO
# PASO 5: Filtrar por Estado (si está el parámetro)
# PASO 6: Filtrar por rango (si está el parametro)
# PASO 7: Validación de combinación repetida (DNI+Nro de Cheque+Nro de cuenta)
# PASO 8: Imprimir por pantalla
# PASO 9: Exportar CSV    

import csv
import os
import sys
from datetime import datetime

if (len(sys.argv) < 5) or (len(sys.argv) > 7):
    print("ERROR - revise la cantidad de parametros ingresados(ingresó",len(sys.argv),"parametros)")
    quit()

path = sys.argv[1].strip()   #el csv que abrimos con la info de los cheques, es otro que el csv que tenemos que exportar al final
dni = sys.argv[2]
salida = sys.argv[3].upper()
tipo = sys.argv[4].upper()
estado = sys.argv[5].upper() if len(sys.argv) > 5 else None
fecha = sys.argv[6] if len(sys.argv) > 6 else None



if not os.path.exists(path) or not os.path.isfile(path):
    print("el archivo no existe")
    quit()

try:
    file =  open (path, "r")
except:
    print("ERROR - no se puede abrir el archivo")

try:
    dni = int(dni)
except:
    print("ERROR - ingrese DNI solo numeros")   #test.csv, 1209310293,PANTALLA,EMITIDO,PENDIENTE, 25-02-1997:03-07-2022 
                                                #python3 listado_chesques.py test.csv, 11580999, PANTALLA, emitido, aprobado, 04-04-2021:06-04-2021

if salida != "PANTALLA" and salida != "CSV":
    print("ERROR - el parametro debe ser 'PANTALLA' o 'CSV' ")

if tipo != "EMITIDO" and tipo != "DEPOSITADO":
    print("ERROR - el parametro debe ser 'EMITIDO' o 'DEPOSITADO' ")

if estado != "PENDIENTE" and estado != "APROBADO" and estado != "RECHAZADO" and estado != None:
    print("ERROR - el parametro debe ser 'PENDIENTE','APROBADO' o 'RECHAZADO' ")

if fecha != None:
    try:
        fechastr = fecha.split(":")
        dia1,mes1,ano1 = fechastr[0].split("-")
        dia2,mes2,ano2 = fechastr[1].split("-")
        fechaorigen = datetime(int(ano1), int(mes1), int(dia1))
        fechaorigents = fechaorigen.timestamp()
        fechapago = datetime(int(ano2),int(mes2),int(dia2))
        fechapagots = fechapago.timestamp()
    except:
        print("ERROR - ingrese fecha valida ")
        pass




print("Ud. ingresó: ",path,dni,salida,tipo,estado,fecha)  

# lo de arriba es la parte de verificacion de datos -------------------------------------------------------------

#hay que ver si se repite la combinacion: dni + n cheque + n cuenta, si pasa eso devolver error
filtro1 = []
filtro2 = []
filtro3 = [["NroCheque","CodigoBanco","CodigoSucursal","NumeroCuentaOrigen","NumeroCuentaDestino","Valor","FechaOrigen","FechaPago","DNI","Tipo","Estado"]]
checkdup=[]

reader = csv.reader(file)
for fila in reader:
    checkdup.append(str([fila[8]+fila[0]+fila[3]]))

    if fila[8] == str(dni) and fila[9] == tipo:
        filtro1.append(fila) 

if len(checkdup) != len(set(checkdup)):
    print("ERROR - Numero de cheque repetido para esta cuenta y este dni!")
else: 
    pass

for fila in filtro1:
    if estado != None and fila[10] == estado:
        filtro2.append(fila)
    elif estado == None:
        filtro2.append(fila)

for fila in filtro2:
    if fecha != None and tipo == "EMITIDO" and int(fila[6]) >= int(fechaorigents):
        filtro3.append(fila)
        
    elif fecha != None and tipo == "Depositado" and int(fila[7]) <= int(fechapagots):
        filtro3.append(fila)
        
    elif fecha == None:
        filtro3.append(fila)

filtro4 = []
for fila in filtro3:
    fila = [fila[3],fila[5],fila[6],fila[7]]
    filtro4.append(fila)

#esta es la parte de la salida, la ponemos al final pq primero hay que "fabricar" los csv que se van a imprimir o exportar

if salida == "PANTALLA":
    print("--------------------------------------------------------------")
    print("Imprimiendo en pantalla:")
    for fila in filtro3:
        print(fila)
    print("--------------------------------------------------------------")

elif salida == "CSV":
    ts = int(datetime.now().timestamp())
    fname = str(dni)+str(ts)+".csv"
    with open (fname,"w") as file:
        print("writing csv file...")
        writer = csv.writer(file)
        writer.writerows(filtro4) 
    print("csv done:",fname)  

 

