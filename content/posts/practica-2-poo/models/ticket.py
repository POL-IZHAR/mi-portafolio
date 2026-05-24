from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from models.vehicle import Vehicle
from models.spot import ParkingSpot

@dataclass
class Ticket:
    id_ticket: int
    vehiculo: Vehicle
    spot: ParkingSpot
    hora_entrada: datetime
    estado: str = "ACTIVE"
    hora_salida: Optional[datetime] = None
    costo: float = 0.0

    def cerrar(self, hora_salida: datetime):
        self.hora_salida = hora_salida
        self.estado = "CLOSED"