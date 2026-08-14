from flask import Flask, jsonify, render_template
import csv

app = Flask(__name__)
def analyze_vehicle(vehicle):
    temperature = float(vehicle["temperature"])
    fuel = float(vehicle["fuel_consumption"])

    if temperature > 100 or fuel > 15:
        status = "Critical"
    elif temperature >= 80 or fuel >= 10:
        status = "Warning"
    else:
        status = "Normal"

    return status

def load_vehicles():
    vehicles = []

    with open("data/vehicles.csv", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            vehicles.append(row)

    return vehicles


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/vehicles")
def get_vehicles():
    vehicles = load_vehicles()
    
    for vehicle in vehicles:
        vehicle["Smart Status"] = analyze_vehicle(vehicle)
    return jsonify(vehicles)


@app.route("/api/vehicles/<vehicle_id>")
def get_vehicle(vehicle_id):
    vehicles = load_vehicles()

    for vehicle in vehicles:
        if vehicle["vehicle_id"] == vehicle_id:
            return jsonify(vehicle)

    return jsonify({"error": "Vehicle not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
