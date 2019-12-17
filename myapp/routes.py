from myapp import app
from flask import render_template
import csv

@app.route('/')
def index():
    fSales = open('../sales10.csv', 'r')
    csvreader = csv.reader(fSales, delimiter=',')
    registros = []
    for linea in csvreader:
        registros.append(linea)

    cabecera = registros[0]
    ventas = []
    for datos in registros[1:]:
        d = {}
        for ix, nombre_campo in enumerate(cabecera): #delego todo el control en python
            d[nombre_campo] = datos[ix]    
        ventas.append(d)
        '''
        otras formas de hacer lo mismo
        i = 0
        for nombre_campo in cabecera: #delego el control del nombre y yo llevo el indice
            d[nombre_campo] = datos[i]
            i += 1
        
        for ix in range (len(cabecera)): #delego el control del indice y yo llevo el nombre
            nombre_campo = cabecera[ix]
            d[nombre_campo]= datos [ix]
        '''   
        resultado = [] #lista de diccionarios
        '''
        recorrer el diccionario creando uno nuevo con region, ingresos totales y beneficios totales
        '''
    return render_template('index.html', registros=resultados)

@app.route("/detail")
def detail():
    return render_template('detail.html')