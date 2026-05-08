from cliente import Cliente

from servicio import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from reserva import Reserva

from logger import registrar_log

from excepciones import (
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaError,
    DuracionInvalidaError
)

clientes = []

reservas = []


print("\n========== SOFTWARE FJ ==========\n")


# ======================================
# OPERACIÓN 1
# ======================================

try:

    cliente1 = Cliente(
        "Juan Perez",
        "123456",
        "juan@gmail.com",
        "3001112233"
    )

    clientes.append(cliente1)

    registrar_log(
        "Cliente Juan registrado."
    )

except ClienteInvalidoError as e:

    registrar_log(e)


# ======================================
# OPERACIÓN 2 (ERROR)
# ======================================

try:

    cliente2 = Cliente(
        "",
        "ABC",
        "correo_mal",
        "telefono"
    )

    clientes.append(cliente2)

except ClienteInvalidoError as e:

    registrar_log(
        f"Error cliente inválido: {e}"
    )

    print(f"ERROR: {e}")


# ======================================
# CREAR SERVICIOS
# ======================================

try:

    sala = ReservaSala(
        "Sala Premium",
        100000
    )

    equipo = AlquilerEquipo(
        "Portátiles",
        80000
    )

    asesoria = AsesoriaEspecializada(
        "Asesoría Python",
        120000
    )

except ServicioNoDisponibleError as e:

    registrar_log(e)


# ======================================
# OPERACIÓN 3
# ======================================

try:

    reserva1 = Reserva(
        cliente1,
        sala,
        2
    )

    costo = reserva1.procesar()

    reserva1.confirmar()

    reservas.append(reserva1)

    print(
        f"Reserva exitosa. "
        f"Costo: ${costo}"
    )

except Exception as e:

    registrar_log(e)


# ======================================
# OPERACIÓN 4
# ======================================

try:

    reserva2 = Reserva(
        cliente1,
        equipo,
        3
    )

    costo = reserva2.procesar()

    reserva2.confirmar()

    reservas.append(reserva2)

    print(
        f"Reserva exitosa. "
        f"Costo: ${costo}"
    )

except Exception as e:

    registrar_log(e)


# ======================================
# OPERACIÓN 5
# ======================================

try:

    reserva3 = Reserva(
        cliente1,
        asesoria,
        1
    )

    costo = reserva3.procesar()

    reserva3.confirmar()

    reservas.append(reserva3)

    print(
        f"Reserva exitosa. "
        f"Costo: ${costo}"
    )

except Exception as e:

    registrar_log(e)


# ======================================
# OPERACIÓN 6 (ERROR)
# ======================================

try:

    reserva4 = Reserva(
        cliente1,
        sala,
        -5
    )

    costo = reserva4.procesar()

except DuracionInvalidaError as e:

    registrar_log(e)

    print(f"ERROR: {e}")


# ======================================
# OPERACIÓN 7
# ======================================

try:

    reserva5 = Reserva(
        cliente1,
        equipo,
        5
    )

    costo = reserva5.procesar()

    reserva5.cancelar()

    reservas.append(reserva5)

except ReservaError as e:

    registrar_log(e)


# ======================================
# OPERACIÓN 8 (ERROR)
# ======================================

try:

    servicio_malo = ReservaSala(
        "Sala dañada",
        -1000
    )

    servicio_malo.validar_servicio()

except ServicioNoDisponibleError as e:

    registrar_log(e)

    print(f"ERROR: {e}")


# ======================================
# OPERACIÓN 9
# ======================================

try:

    cliente3 = Cliente(
        "Maria Lopez",
        "789456",
        "maria@gmail.com",
        "3119998877"
    )

    clientes.append(cliente3)

    reserva6 = Reserva(
        cliente3,
        asesoria,
        2
    )

    costo = reserva6.procesar()

    reserva6.confirmar()

    reservas.append(reserva6)

except Exception as e:

    registrar_log(e)


# ======================================
# OPERACIÓN 10
# ======================================

try:

    cliente4 = Cliente(
        "Carlos Ruiz",
        "456123",
        "carlos@gmail.com",
        "3208887766"
    )

    clientes.append(cliente4)

    reserva7 = Reserva(
        cliente4,
        sala,
        4
    )

    costo = reserva7.procesar()

    reserva7.confirmar()

    reservas.append(reserva7)

except Exception as e:

    registrar_log(e)


# ======================================
# MOSTRAR RESULTADOS
# ======================================

print("\n========== CLIENTES ==========\n")

for cliente in clientes:

    print(cliente.mostrar_info())


print("\n========== RESERVAS ==========\n")

for r in reservas:

    print(
        f"Cliente: {r.cliente.get_nombre()} | "
        f"Servicio: {r.servicio.nombre} | "
        f"Estado: {r.estado}"
    )

print("\nSistema ejecutado correctamente.")
