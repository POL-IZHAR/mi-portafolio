from dataclasses import dataclass

@dataclass
class Vehicle:
    placas: str
    tipo: str

@dataclass
class Car(Vehicle):
    tipo: str = "Car"

@dataclass
class Motorcycle(Vehicle):
    tipo: str = "Motorcycle"