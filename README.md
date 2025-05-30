# Trabajo Práctico Final (Evaluación 2do parcial) - Sistema de Turnos

## 🏥 Trabajo Práctico: Sistema de Gestión de Turnos Médicos

### 🎯 Objetivo General
Diseñar una aplicación de consola en Python que permita gestionar pacientes, médicos y turnos médicos, aplicando principios de POO, validación de datos y persistencia con archivos binarios usando `pickle`.

## 🧱 Entidades y Atributos
### 1. Paciente
- **DNI** (único)
- **Nombre**
- **Obra social** (opcional)
- **Fecha de nacimiento** (usando clase `Fecha`)

### 2. Médico
- **Matrícula** (única)
- **Nombre**
- **Especialidad** (cardiología, pediatría, etc.)

### 3. Turno
- **Fecha y hora** (clase `Fecha` + hora en formato `HH:MM`)
- **Paciente** (referencia al DNI)
- **Médico** (referencia a la matrícula)
- **Motivo del turno** (texto)

## 🔁 Relaciones
- Un **paciente** puede tener muchos turnos.
- Un **médico** puede tener muchos turnos.
- Un **turno** siempre pertenece a un solo médico y un solo paciente.

## 🖥 Menú Principal
- Gestión de pacientes
- Gestión de médicos
- Gestión de turnos
- Salir

## 📂 Submenús (CRUD)
### 📌 Gestión de Pacientes
- Listar todos
- Buscar por DNI
- Agregar
- Modificar (**nombre, obra social, fecha de nacimiento**)
- Eliminar
- Guardar cambios

### 📌 Gestión de Médicos
- Listar todos
- Buscar por matrícula
- Agregar
- Modificar (**nombre, especialidad**)
- Eliminar
- Guardar cambios

### 📌 Gestión de Turnos
- Listar todos
- Listar turnos por **paciente** o por **médico**
- Buscar por **fecha**
- Agregar (**verificar que paciente y médico existan**)
- **Evitar solapamiento** de turnos (**un médico no puede tener dos turnos a la misma hora**)
- Eliminar
- Guardar cambios

## 📅 Clase Fecha (reutilizable)
Se proporciona una nueva versión de la clase `Fecha` trabajada en clases con el agregado de las **horas y minutos**, la nueva clase se llama `FechaHora`.

## 💡 Extras opcionales (para más desafío)
- Validar que los turnos sean en el futuro.
- Generar un informe (**por ejemplo: cantidad de turnos por médico**).
- Generar identificadores únicos automáticos para los turnos.
- Persistir también en formato **CSV** para **importar/exportar**.

## 💾 Persistencia
Usar `pickle` para guardar:
- `pacientes.bin`
- `medicos.bin`
- `turnos.bin`

## 📦 Organización sugerida
- **Paciente, Medico, Turno, Fecha** (clases modelo)
- **GestorDePacientes, GestorDeMedicos, GestorDeTurnos** (gestores CRUD)
- **Menú y submenús**
- **Función `main()` para ejecución**