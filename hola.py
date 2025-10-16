""" CONTEXTO GENERAL DEL PROYECTO

Proyecto: Sistema de gestión para gimnasio
Stack técnico:

Backend: Django 4+ con SQLite3 (DB por defecto)

Frontend: React + Vite + Bootstrap (última versión)

API: Django REST Framework (DRF)

HTTP Client: Axios (frontend → backend)

 MODELOS DJANGO (en models.py)

Generá los siguientes modelos con relaciones y campos especificados:

Usuario

id_usuario (AutoField, PK)

nombre_usuario (str, único)

contraseña (hashed)

rol (choices: Administrador, Profesor, Socio)

estado (choices: Activo, Inactivo)

Socio

id_socio (AutoField, PK)

nombre, apellido, dni, fecha_nacimiento, telefono, email, direccion

Plan

id_plan, nombre_plan, descripcion, precio

Membresia

id_membresia

socio (FK a Socio)

plan (FK a Plan)

fecha_inicio, fecha_fin, estado (Activa, Vencida, Congelada)

Pago

id_pago

socio (FK a Socio)

fecha_pago, monto, metodo_pago, estado (Pendiente, Completado, Anulado)

Asistencia

id_asistencia

socio (FK a Socio)

fecha_hora_entrada, fecha_hora_salida

Clase

id_clase, nombre_clase, descripcion, horario, cupo_maximo

profesor (FK a Usuario)

Reserva

id_reserva

socio (FK a Socio)

clase (FK a Clase)

fecha_reserva, estado (Confirmada, Cancelada)

Rutina

id_rutina

socio (FK a Socio)

profesor (FK a Usuario)

descripcion, fecha_asignacion

 API DJANGO

Usar Django REST Framework

Serializers para cada modelo

Rutas para CRUD básicas

Autenticación basada en tokens (SimpleJWT)

 FRONTEND (React + Vite + Bootstrap)

Estructura modular por roles (Admin, Profesor, Socio) con componentes para:

Socios:

Registrar ingreso

Ver rutina

Ver estado de cuenta

Reservar/cancelar clase

Ver historial de asistencias

Profesores:

Asignar rutinas

Gestionar clases

Visualizar agenda

Administradores:

CRUD de socios, clases, usuarios

Registrar pagos

Generar reportes (deudores, asistencia)

Consultar estado de cuenta


🔌 CONEXIÓN AXIOS
Crear archivo api/axios.js o axios.ts
Base URL: http://localhost:8000/api/
Headers con Authorization si usa tokens """