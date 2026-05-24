from models.vehicle import Car, Motorcycle
from models.spot import ParkingSpot
from models.rates import HourlyRatePolicy
from models.parking_lot import ParkingLot

def main():
    spots = [
        ParkingSpot("A1", "Car"), ParkingSpot("A2", "Car"),
        ParkingSpot("M1", "Motorcycle"), ParkingSpot("M2", "Motorcycle")
    ]
    policy = HourlyRatePolicy()
    estacionamiento = ParkingLot(spots, policy)

    while True:
        print("\n1. Registrar entrada")
        print("2. Registrar salida")
        print("3. Ver ocupación")
        print("4. Ver tickets activos")
        print("5. Salir")
        
        opcion = input("Opcion: ")

        if opcion == "1":
            placas = input("Placas: ")
            tipo = input("Tipo (Car/Motorcycle): ")
            try:
                if tipo == "Car":
                    vehiculo = Car(placas=placas)
                elif tipo == "Motorcycle":
                    vehiculo = Motorcycle(placas=placas)
                else:
                    raise ValueError("Tipo de vehículo no válido")

                ticket = estacionamiento.registrar_entrada(vehiculo)
                print(f"Ticket #{ticket.id_ticket}, spot={ticket.spot.id_spot}")
            except ValueError as e:
                print(e)

        elif opcion == "2":
            try:
                ticket_id = int(input("ID Ticket: "))
                horas = float(input("Horas (simulado): "))
                ticket = estacionamiento.registrar_salida(ticket_id, horas)
                print(f"Tiempo={horas}h costo=${ticket.costo} spot liberado={ticket.spot.id_spot}")
            except ValueError as e:
                print(e)

        elif opcion == "3":
            libres, ocupados = estacionamiento.ver_ocupacion()
            print(f"Libres={libres} Ocupados={ocupados}")

        elif opcion == "4":
            tickets = estacionamiento.ver_tickets_activos()
            lista_ids = [f"#{t.id_ticket}" for t in tickets]
            print(f"Tickets activos: {lista_ids}")

        elif opcion == "5":
            break

if __name__ == "__main__":
    main()