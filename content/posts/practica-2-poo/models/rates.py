from typing import Protocol
from models.vehicle import Vehicle

class RatePolicy(Protocol):
    def calculate(self, hours: float, vehicle: Vehicle) -> float:
        pass

class FlatRatePolicy:
    def calculate(self, hours: float, vehicle: Vehicle) -> float:
        if vehicle.tipo == "Car":
            return 40.0
        return 20.0

class HourlyRatePolicy:
    def calculate(self, hours: float, vehicle: Vehicle) -> float:
        tarifa_base = 20.0 if vehicle.tipo == "Car" else 10.0
        return tarifa_base * hours