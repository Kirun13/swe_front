import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")




@app.route('/driver')
def driver():
    return render_template("internal/driver/driver_main.html")

@app.route('/driver_active_routes')
def driver_active_routes():
    return render_template("internal/driver/driver_active_routes.html")

@app.route('/driver_routes_history')
def driver_routes_history():
    return render_template("internal/driver/driver_routes_history.html")

@app.route('/driver_vehicle')
def driver_vehicle():
    return render_template("internal/driver/driver_vehicle.html")




@app.route('/maintenance')
def maintenance():
    return render_template("internal/maintenance/maintenance_main.html")

@app.route('/maintenance_assignments')
def maintenance_assignments():
    return render_template("internal/maintenance/maintenance_assignments.html")

@app.route('/maintenance_request_parts')
def maintenance_request_parts():
    return render_template("internal/maintenance/maintenance_request_parts.html")

@app.route('/maintenance_vehicles')
def maintenance_vehicle():
    return render_template("internal/maintenance/maintenance_vehicles.html")



@app.route('/fueling')
def fueling():
    return render_template("internal/fueling/fueling_main.html")

@app.route('/fueling_info')
def fueling_info():
    return render_template("internal/fueling/fueling_info.html")

@app.route('/fueling_vehicle_update')
def fueling_vehicle_update():
    return render_template("internal/fueling/fueling_vehicle_update.html")

@app.route('/add_fueling')
def add_fueling():
    return render_template("internal/fueling/add_fueling.html")


if __name__ == '__main__':
    app.run(debug=True)