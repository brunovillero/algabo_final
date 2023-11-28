import random
from clases.familia import familia
from clases.centro import centro

class generador_de_datos:
    def __init__(self, diccionario_centros):
        #Parametros para generar datos aleatoreos
        self.numero_de_familias = 1000
        self.max_cant_niños_por_familia = 6
        self.min_cant_niños_en_centro = 10
        self.max_cant_niños_en_centro = 50

        #Diccionario de centros ordenados por departamento
        self.diccionario_centros = diccionario_centros

        #Inicializamos variables de resultado
        #Diccionarios donde la key seran los departamentos y los valores las familias o centros dependiendo la variable
        self.familias_por_departamento = {}
        self.centros_por_departamento = {}

    def get_familias_por_departamento(self):
        return self.familias_por_departamento
    
    def get_centros_por_departamento(self):
        return self.centros_por_departamento
    
    def guardar_familia_por_departamento(self, familia):
        if familia.departamento in self.familias_por_departamento:
            self.familias_por_departamento[familia.departamento].append(familia)
        else:
            self.familias_por_departamento[familia.departamento] = [familia]

    def guardar_centro_por_departamento(self, centro):
        if centro.departamento in self.centros_por_departamento:
            self.centros_por_departamento[centro.departamento].append(centro)
        else:
            self.centros_por_departamento[centro.departamento] = [centro]

    def generar(self):
        copia_diccionario_centros = self.diccionario_centros
        departamentos = list(copia_diccionario_centros.keys())

        #Generamos familias
        for id in range(1, self.numero_de_familias + 1):
            #Generamos cantidad de hijos
            cantidad_hijos = random.randint(1, self.max_cant_niños_por_familia)
            
            #Asignamos centros prioritarios aleatoreos en base al departamento
            num_departamento_aleatoreo = random.randint(0, len(departamentos) - 1)
            nombre_departamento_aleatoreo = departamentos[num_departamento_aleatoreo]
            centros_del_departamento = copia_diccionario_centros[nombre_departamento_aleatoreo]
            random.shuffle(centros_del_departamento)
            
            #Guardamos la nueva familia
            familia_obj = familia(id, cantidad_hijos, nombre_departamento_aleatoreo, centros_del_departamento)
            self.guardar_familia_por_departamento(familia_obj)

        #Creamos centros en base a los departamentos de las familias generadas, para asegurar la oferta de las mismas
        for departamento in list(self.familias_por_departamento.keys()):
            centros_del_departamento = self.diccionario_centros[departamento]
            for nombre_centro in centros_del_departamento:
                #Asignamos ranking aleatoreo de familias en base al departamento
                copia_familias_por_departamento = self.familias_por_departamento[departamento]
                random.shuffle(copia_familias_por_departamento)
            
                #Asignamos capacidad maxima aleatorea
                capacidad = random.randint(self.min_cant_niños_en_centro, self.max_cant_niños_en_centro)
                
                #Creamos centros
                centro_obj = centro(nombre_centro, capacidad, departamento, copia_familias_por_departamento)
                self.guardar_centro_por_departamento(centro_obj)