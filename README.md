# Sistema Integral de Gestión - Software FJ

## Descripción del Proyecto

Este proyecto consiste en el desarrollo de un sistema integral de gestión de clientes, servicios y reservas para la empresa ficticia Software FJ. El sistema fue desarrollado en Python utilizando Programación Orientada a Objetos (POO) y manejo avanzado de excepciones, sin uso de bases de datos.

El sistema permite registrar clientes, gestionar diferentes tipos de servicios y procesar reservas de manera segura y organizada, garantizando la estabilidad del programa incluso cuando ocurren errores durante la ejecución.

---

#participantes

jean carlo peña lopez 
dilan salazar peña 
numero 3
numero 4
numero 5

---

# Características del Sistema

- Registro de clientes
- Gestión de servicios
- Gestión de reservas
- Validación de datos
- Manejo avanzado de excepciones
- Registro automático de logs
- Arquitectura modular
- Uso de Programación Orientada a Objetos
- Sistema funcional sin bases de datos

---

# Conceptos de POO Implementados

## Abstracción
Se implementó mediante la clase abstracta `Servicio`.

## Herencia
Las clases:
- `ReservaSala`
- `AlquilerEquipo`
- `AsesoriaEspecializada`

heredan de la clase abstracta `Servicio`.

## Polimorfismo
Cada servicio redefine el método:

```python
calcular_costo()
