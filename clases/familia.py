class familia:
    def __init__(self, id, cantidad_hijos, centros_preferenciales):
        self.id = id
        self.cantidad_hijos = cantidad_hijos
        self.centros_preferenciales = centros_preferenciales
    def get_id(self):
        return self.id
    def get_cantidad_hijos(self):
        return self.cantidad_hijos
    def get_centros_preferenciales(self):
        return self.centros_preferenciales