import csv
from clases.generador_de_datos import generador_de_datos

filen_open = open('./recursos/Nombres_Centros_CAIF_en_Territorio.csv', encoding="utf-8")
file = csv.DictReader(filen_open)

centros = []
for centro in file:
    centros.append(centro["NOMBRE DEL CENTRO"])

#print(centros)

generador = generador_de_datos(centros)
generador.generar()

familias = generador.get_familias()
centros = generador.get_centros()

print(len(familias))
#for familia in familias:
    #print(familia)

print(len(centros))
#for centro in centros:
    #print(centro)