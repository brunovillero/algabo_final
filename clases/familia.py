class familia:
    def __init__(self, id, cantidad_hijos, departamento, centros_preferenciales):
        self.id = id
        self.cantidad_hijos = cantidad_hijos
        self.departamento = departamento
        self.centros_preferenciales = centros_preferenciales
    def get_id(self):
        return self.id
    def get_cantidad_hijos(self):
        return self.cantidad_hijos
    def get_departamento(self):
        return self.departamento
    def get_centros_preferenciales(self):
        return self.centros_preferenciales
    def __str__(self):
        return str(self.id)