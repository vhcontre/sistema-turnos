class Medico:
    def __init__(self, matricula, nombre, especialidad):
        self.matricula = matricula
        self.nombre = nombre
        self.especialidad = especialidad

    def __str__(self):
        return f"Matrícula: {self.matricula} | Nombre: {self.nombre} | Especialidad: {self.especialidad}"
