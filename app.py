import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/driver')
def driver():
    return render_template("driver/driver.html")

@app.route('/login')
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)