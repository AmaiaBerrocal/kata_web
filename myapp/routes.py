from myapp import app
from flask import render_template, request
import csv

fSales = open('./data/sales.csv', 'r') # abrir fichero en modo lectura
csvreader = csv.reader(fSales, delimiter=',') # creo un lector de csv para el fichero sales con la coma como delimitador

registros = [] #va a ser una lista de tuplas
for linea in csvreader: #recorro cada línea de csvreader, separando sus componentes por las comas, haciendo una lista con cada línea
    registros.append(linea) #añado cada lista (cada línea) a resgistros

cabecera = registros[0]
ventas = [] #aquí tenemos cada uno de los registros en forma de diccionario(9 diccionarios)
for datos in registros[1:]:
    d = {}
    for ix, nombre_campo in enumerate(cabecera):
        d[nombre_campo] = datos[ix]    
    ventas.append(d) #meteremos cada uno de los registros en forma de diccionario(9 diccionarios) en ventas

@app.route('/')
def index():  
    datos = {} #creo un diccionario vacio (datos)
    for linea in ventas: #recorro ventas linea por linea y miro la región
        if linea['region'] in datos: #si está la región (ej.Australia) en datos, la recupero y le sumo los ingresos y beneficios
            regAct = datos[linea['region']]
            regAct['ingresos_totales'] += float(linea['ingresos_totales'])
            regAct['beneficios_totales'] += float(linea['beneficio'])
        else: #si no está, la creo en datos{} y le añado los ingresos y beneficios
            datos[linea['region']] = {'ingresos_totales': float(linea['ingresos_totales']), 'beneficios_totales': float(linea['beneficio'])}
    
    resultado = [] #recorro datos, obtengo la clave y creo una tupla con clave-valor. Resultados es una lista de tuplas.
    for clave in datos:
        resultado.append((clave, datos[clave]))
    
    return render_template('index.html', registros=resultado)

@app.route("/detail")
def detail(): #hacemos exactamente lo mismo que en index pero con 'pais'. No metemos los datos en lista para ver como se trabaja con en diccionario
    datos = {}
    region_name = request.values['region']
    for linea in ventas:
        if linea['region'] == region_name: #olo tengo que meter los paises de la region que hemos pedido
            if linea['pais'] in datos:
                regAct = datos[linea['pais']]
                regAct['ingresos_totales'] += float(linea['ingresos_totales'])
                regAct['beneficios_totales'] += float(linea['beneficio'])
            else:
                datos[linea['pais']] = {'ingresos_totales': float(linea['ingresos_totales']), 'beneficios_totales': float(linea['beneficio'])}

    return render_template('detail.html', region=region_name, registros=datos)
