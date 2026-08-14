from flask import Flask, jsonify, render_template
import csv

app = Flask(__name__)


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
