from dataclasses import dataclass

@dataclass
class ParkingSpot:
    id_spot: str
    tipo_permitido: str
    estado: str = "libre"

    def ocupar(self):
        self.estado = "ocupado"

    def liberar(self):
        self.estado = "libre"

    def esta_libre(self) -> bool:
        return self.estado == "libre"