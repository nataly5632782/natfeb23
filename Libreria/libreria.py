class libreria:
    
    def __init__(self,nombre,autor):
        self.nombre=nombre
        self.autor=autor
    def obtenernombre(self):
        return f'el libro es: {self.nombre} el autor es: {self.autor}'