import csv
from clases.generador_de_datos import generador_de_datos

filen_open = open('./resources/Nombres_Centros_CAIF_en_Territorio.csv', encoding="utf-8")
file = csv.DictReader(filen_open)

centros = []
for centro in file:
    centros.append(centro["NOMBRE DEL CENTRO"])

generador = generador_de_datos(centros)
generador.generar()
