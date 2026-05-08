from abc import ABC, abstractmethod

from excepciones import ServicioNoDisponibleError


# CLASE ABSTRACTA
class Servicio(ABC):

    def __init__(self, nombre, precio_base):

        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, duracion, descuento=0):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def validar_servicio(self):
        pass


# ======================================
# SERVICIO 1
# ======================================

class ReservaSala(Servicio):

    def calcular_costo(self, duracion, descuento=0):

        total = self.precio_base * duracion

        total -= total * descuento

        return total

    def descripcion(self):

        return "Servicio de reserva de salas."

    def validar_servicio(self):

        if self.precio_base <= 0:

            raise ServicioNoDisponibleError(
                "Precio inválido para reserva de sala."
            )


# ======================================
# SERVICIO 2
# ======================================

class AlquilerEquipo(Servicio):

    def calcular_costo(self, duracion, descuento=0):

        total = (self.precio_base * duracion) + 50000

        total -= total * descuento

        return total

    def descripcion(self):

        return "Servicio de alquiler de equipos."

    def validar_servicio(self):

        if self.precio_base <= 0:

            raise ServicioNoDisponibleError(
                "Precio inválido para alquiler."
            )


# ======================================
# SERVICIO 3
# ======================================

class AsesoriaEspecializada(Servicio):

    def calcular_costo(self, duracion, descuento=0):

        total = (self.precio_base * duracion) * 1.19

        total -= total * descuento

        return total

    def descripcion(self):

        return "Servicio de asesoría especializada."

    def validar_servicio(self):

        if self.precio_base <= 0:

            raise ServicioNoDisponibleError(
                "Precio inválido para asesoría."
            )
            