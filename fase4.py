    cliente = Cliente(
        "",
        "laura@gmail.com",
        "3101234567"
    )
    sistema_pruebas.registrar_cliente(cliente)


def prueba3():
    cliente = Cliente(
        "Luis Gómez",
        "correo_incorrecto",
        "3201234567"
    )
    sistema_pruebas.registrar_cliente(cliente)


def prueba4():
    sala = ReservaSala("Sala principal", 50000)
    sistema_pruebas.registrar_servicio(sala)


def prueba5():
    sala = ReservaSala("Sala incorrecta", -20000)
    sistema_pruebas.registrar_servicio(sala)


def prueba6():
    equipo = AlquilerEquipo("Computador", 30000)
    sistema_pruebas.registrar_servicio(equipo)


def prueba7():
    asesoria = Asesoria("Programación", 80000)
    sistema_pruebas.registrar_servicio(asesoria)


def prueba8():
    cliente = sistema_pruebas.clientes[0]
    servicio = sistema_pruebas.servicios[0]

    reserva = Reserva(cliente, servicio, 3)

    sistema_pruebas.registrar_reserva(reserva)

    reserva.confirmar()
    reserva.procesar()


def prueba9():
    cliente = sistema_pruebas.clientes[0]
    servicio = sistema_pruebas.servicios[0]

    reserva = Reserva(cliente, servicio, -3)

    sistema_pruebas.registrar_reserva(reserva)


def prueba10():
    reserva = sistema_pruebas.reservas[0]
    reserva.cancelar()


def prueba11():
    reserva = sistema_pruebas.reservas[0]
    reserva.confirmar()


def prueba12():
    servicio = sistema_pruebas.servicios[0]

    total = servicio.calcular_costo(
        2, impuesto=19, descuento=10
    )

    print("Costo total: $", total)

def main():
    global sistema_pruebas
    logging.info("Sistema Software FJ iniciado")
    sistema_pruebas = SistemaSoftwareFJ()
    print("\n========== SIMULACIÓN SOFTWARE FJ ==========")

    pruebas = [
        ("Registrar cliente válido", prueba1),
        ("Cliente sin nombre", prueba2),
        ("Correo inválido", prueba3),
        ("Crear servicio de sala", prueba4),
        ("Servicio con precio negativo", prueba5),
        ("Crear alquiler de equipo", prueba6),
        ("Crear asesoría", prueba7),
        ("Reserva exitosa", prueba8),
        ("Reserva con horas negativas", prueba9),
        ("Cancelar reserva", prueba10),
        ("Confirmar reserva cancelada", prueba11),
        ("Calcular impuestos y descuentos", prueba12),
    ]

    for numero, (descripcion, funcion) in enumerate(pruebas, 1):
        ejecutar_prueba(numero, descripcion, funcion)

    sistema_pruebas.mostrar_resumen()
    print("\nSIMULACIÓN FINALIZADA")
    logging.info("Finalizaron las 12 operaciones de prueba")

    print("\n--- PRUEBA ADICIONAL: CLIENTE DUPLICADO ---")
    try:
        duplicado = Cliente("Otro Pedro", "pedro@gmail.com", "3119999999")
        sistema_pruebas.registrar_cliente(duplicado)
    except ErrorCliente as error:
        print("Error controlado:", error)
        logging.error("Cliente duplicado: %s", error)

    print("\n--- PRUEBA DE ENCADENAMIENTO DE EXCEPCIONES ---")
    try:
        crear_reserva_segura(sistema_pruebas.clientes[0], sistema_pruebas.servicios[0], 0)
    except ErrorReserva as error:
        print("Error controlado:", error)
        print("Causa original:", error.__cause__)
        logging.error("Error personalizado: %s. Causa: %s", error, error.__cause__)


if __name__ == "__main__":
    main()

