from flask import Flask, request, render_template, redirect, url_for
from models.vehicle import Car, Motorcycle
from models.spot import ParkingSpot
from models.rates import HourlyRatePolicy
from models.parking_lot import ParkingLot

app = Flask(__name__)

# Instancia global del modelo (Persistencia en memoria)
spots = [
    ParkingSpot("A1", "Car"), ParkingSpot("A2", "Car"),
    ParkingSpot("M1", "Motorcycle"), ParkingSpot("M2", "Motorcycle")
]
policy = HourlyRatePolicy()
mi_estacionamiento = ParkingLot(spots, policy)

@app.route('/')
def dashboard():
    mensaje = request.args.get('mensaje', '')
    error = request.args.get('error', '')
    libres, ocupados = mi_estacionamiento.ver_ocupacion()
    tickets = mi_estacionamiento.ver_tickets_activos()
    return render_template('dashboard.html', libres=libres, ocupados=ocupados, tickets=tickets, mensaje=mensaje, error=error)

@app.route('/entry', methods=['GET', 'POST'])
def entry():
    if request.method == 'POST':
        placa = request.form.get('placa')
        tipo = request.form.get('tipo')
        try:
            vehiculo = Car(placas=placa) if tipo == "Car" else Motorcycle(placas=placa)
            ticket = mi_estacionamiento.registrar_entrada(vehiculo)
            return redirect(url_for('dashboard', mensaje=f"Vehículo {placa} ingresado. Ticket #{ticket.id_ticket} en espacio {ticket.spot.id_spot}."))
        except Exception as e:
            return redirect(url_for('dashboard', error=str(e)))
    return render_template('entry.html')

@app.route('/exit', methods=['GET', 'POST'])
def exit():
    if request.method == 'POST':
        try:
            ticket_id = int(request.form.get('ticket_id'))
            horas = float(request.form.get('horas'))
            ticket = mi_estacionamiento.registrar_salida(ticket_id, horas)
            return redirect(url_for('dashboard', mensaje=f"Salida procesada. Costo: ${ticket.costo}. Espacio {ticket.spot.id_spot} liberado."))
        except Exception as e:
            return redirect(url_for('dashboard', error=str(e)))
    return render_template('exit.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)