from typing import List, Optional
from datetime import datetime
from models.spot import ParkingSpot
from models.ticket import Ticket
from models.vehicle import Vehicle
from models.rates import RatePolicy

class ParkingLot:
    def __init__(self, spots: List[ParkingSpot], rate_policy: RatePolicy):
        self._spots = spots
        self._tickets_activos: List[Ticket] = []
        self._rate_policy = rate_policy
        self._next_ticket_id = 1
        self._total_recaudado = 0.0

    def registrar_entrada(self, vehiculo: Vehicle) -> Ticket:
        spot = self._buscar_spot_compatible(vehiculo)
        if not spot:
            raise ValueError("Estacionamiento lleno o sin spot compatible")

        spot.ocupar()
        ticket = Ticket(
            id_ticket=self._next_ticket_id,
            vehiculo=vehiculo,
            spot=spot,
            hora_entrada=datetime.now()
        )
        self._tickets_activos.append(ticket)
        self._next_ticket_id += 1
        return ticket

    def registrar_salida(self, ticket_id: int, hours: float) -> Ticket:
        ticket = self._buscar_ticket(ticket_id)
        if not ticket:
            raise ValueError("Ticket no encontrado / inválido")

        ticket.cerrar(datetime.now())
        costo = self._rate_policy.calculate(hours, ticket.vehiculo)
        ticket.costo = costo
        ticket.spot.liberar()
        
        self._tickets_activos.remove(ticket)
        self._total_recaudado += costo
        return ticket

    def _buscar_spot_compatible(self, vehiculo: Vehicle) -> Optional[ParkingSpot]:
        for spot in self._spots:
            if spot.esta_libre() and spot.tipo_permitido == vehiculo.tipo:
                return spot
        return None

    def _buscar_ticket(self, ticket_id: int) -> Optional[Ticket]:
        for ticket in self._tickets_activos:
            if ticket.id_ticket == ticket_id:
                return ticket
        return None

    def ver_ocupacion(self):
        libres = sum(1 for spot in self._spots if spot.esta_libre())
        ocupados = len(self._spots) - libres
        return libres, ocupados

    def ver_tickets_activos(self) -> List[Ticket]:
        return self._tickets_activos