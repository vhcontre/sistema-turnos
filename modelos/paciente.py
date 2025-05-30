class Paciente:
    def __init__(self, dni, nombre, fecha_nacimiento, obra_social=""):
        self.dni = dni
        self.nombre = nombre
        self.obra_social = obra_social
        self.fecha_nacimiento = fecha_nacimiento  # Instancia de FechaHora

    def __str__(self):
        return f"DNI: {self.dni} | Nombre: {self.nombre} | Obra Social: {self.obra_social} | Nacimiento: {self.fecha_nacimiento}"
