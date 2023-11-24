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

@app.route('/driver_route_details')
def driver_route_details():
    return render_template("internal/driver/driver_route_details.html")


if __name__ == '__main__':
    app.run(debug=True)