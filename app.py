import csv
from clases.generador_de_datos import generador_de_datos
from clases.gale_shapley import gale_shapley

filen_open = open('./recursos/Nombres_Centros_CAIF_en_Territorio.csv', encoding="utf-8")
file = csv.DictReader(filen_open)

def procesar_archivo(archivo):
    #Agrupar centros por departamento
    centros = {}
    for centro in archivo:
        nombre = centro["NOMBRE DEL CENTRO"]
        departamento = centro["DEPARTAMENTO"]
        if departamento in centros:
            centros[departamento].append(nombre)
        else:
            centros[departamento] = [nombre]
    return centros

#Simulacion de datos
centros = procesar_archivo(file)
generador = generador_de_datos(centros)
generador.generar()

contador = 0
contador2 = 0
for departamento_familias in generador.get_familias_por_departamento():
    contador2 += 1
    for familia in generador.get_familias_por_departamento()[departamento_familias]:
        contador += 1

print(contador)

contador = 0
contador2 = 0
for departamento_centros in generador.get_centros_por_departamento():
    contador2 += 1
    for centro in generador.get_centros_por_departamento()[departamento_centros]:
        contador += 1
print(contador)

gale_shapley(generador.get_familias_por_departamento(), generador.get_centros_por_departamento())

#print(generador.get_centros_por_departamento()['RIVERA'][0].familias_preferenciales)



