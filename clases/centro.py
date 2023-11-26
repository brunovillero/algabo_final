class centro:
    def __init__(self, nombre, capacidad_max, departamento, familias_preferenciales):
        self.nombre = nombre
        self.capacidad_max = capacidad_max
        self.departamento = departamento
        self.familias_preferenciales = familias_preferenciales
    def get_nombre(self):
        return self.nombre
    def get_capacidad_max(self):
        return self.capacidad_max
    def get_departamento(self):
        return self.departamento
    def get_familias_preferenciales(self):
        return self.familias_preferenciales
    def __str__(self):
        return self.nombre