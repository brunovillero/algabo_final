import random
from clases.familia import familia
from clases.centro import centro

class generador_de_datos:
    def __init__(self, nombres_de_centros):
        #Parametros para generar datos aleatoreos
        self.numero_de_familias = 1000
        self.max_cant_de_centros_pref_familias = 5
        self.max_cant_niños_por_familia = 6
        self.min_cant_niños_en_centro = 10
        self.max_cant_niños_en_centro = 50
        #Lista de centros
        self.nombres_de_centros = nombres_de_centros
        #Inicializamos variables de resultado
        self.familias = []
        self.centros = []
    def get_familias(self):
        return self.familias
    def get_centros(self):
        return self.centros
    def generar(self):

        copia_centros = self.nombres_de_centros
        #Generamos familias
        for id in range(1, self.numero_de_familias):
            #Generamos cantidad de hijos
            cantidad_hijos = random.randint(1, self.max_cant_niños_por_familia)
            #Asignamos centros aleatoreos
            random.shuffle(copia_centros)
            centros_pref_familia = copia_centros[ 0 : self.max_cant_de_centros_pref_familias - 1]
            #Guardamos la nueva familia
            familia_obj = familia(id, cantidad_hijos, centros_pref_familia)
            self.familias.append(familia_obj)
        
        copia_familias = self.familias
        #Generamos centros
        for nombre_centro in self.nombres_de_centros:
            #Asignamos ranking aleatoreo
            random.shuffle(copia_familias)
            #Asignamos capacidad maxima aleatorea
            capacidad = random.randint(self.min_cant_niños_en_centro, self.max_cant_niños_en_centro)
            #Creamos centros
            centro_obj = centro(nombre_centro, capacidad, copia_familias)
            self.centros.append(centro_obj)