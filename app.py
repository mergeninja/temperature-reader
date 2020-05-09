from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/temperatures", methods=["GET"])
def current_temperatures():
    return jsonify(read_temperatures())

@app.route("/temperatures/store", methods=["POST"])
def store_temperatures():
    temperatures = current_temperatures()
    # save the temperatures to a database or file
    return "", 204 # 204 is the http status for success, but no response body



def read_temperatures():
    # read all the temperatures
    return {
            "sensor_1": 1.23,
            "sensor_2": 4.56,
    }
    


