from excepciones import (
    ReservaError,
    DuracionInvalidaError
)

from logger import registrar_log


class Reserva:

    def __init__(self, cliente, servicio, duracion):

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

        if duracion <= 0:

            raise DuracionInvalidaError(
                "La duración debe ser mayor que cero."
            )

        self.duracion = duracion

    def confirmar(self):

        self.estado = "Confirmada"

        registrar_log(
            f"Reserva confirmada para "
            f"{self.cliente.get_nombre()}"
        )

    def cancelar(self):

        self.estado = "Cancelada"

        registrar_log(
            f"Reserva cancelada para "
            f"{self.cliente.get_nombre()}"
        )

    def procesar(self):

        try:

            self.servicio.validar_servicio()

            costo = self.servicio.calcular_costo(
                self.duracion
            )

        except Exception as error:

            registrar_log(
                f"Error procesando reserva: {error}"
            )

            raise ReservaError(
                "No fue posible procesar la reserva."
            ) from error

        else:

            registrar_log(
                f"Reserva procesada correctamente "
                f"para {self.cliente.get_nombre()}"
            )

            return costo

        finally:

            registrar_log(
                "Proceso de reserva finalizado."
            )