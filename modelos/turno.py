from utils.fecha import Fecha



"""
_ultimo_numero NO debe ser un atributo de instancia, sino de clase.
¿Por qué?
Porque si lo hago como atributo de instancia (self._ultimo_numero), cada turno tendría su propio contador 
y el número no sería autoincremental entre diferentes instancias de Turno.
Como atributo de clase (Turno._ultimo_numero), todos los objetos Turno comparten el mismo contador.
"""
class Turno:
    
    _ultimo_numero = 0  # Atributo de clase para autoincrementar

    def __init__(self, fecha_hora, paciente_dni, medico_matricula, motivo):
        Turno._ultimo_numero += 1
        self.numero = Turno._ultimo_numero  # Número autoincremental
        self.fecha_hora = fecha_hora  # Instancia de FechaHora
        self.paciente_dni = paciente_dni
        self.medico_matricula = medico_matricula
        self.motivo = motivo
        if not isinstance(self.fecha_hora, Fecha):
            raise TypeError("La fecha_hora del turno debe ser una instancia de la clase FechaHora.")

    def __str__(self):
        return f"Turno N°: {self.numero} | {self.fecha_hora} | Paciente DNI: {self.paciente_dni} | Médico Matrícula: {self.medico_matricula} | Motivo: {self.motivo}"
