#!/usr/bin/python

import os
import requests
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

MODEL_FILEPATH = "model.pkl"

if not os.path.exists(MODEL_FILEPATH):
    url = ""
    r = requests.get(url)
    with open(MODEL_FILEPATH, "wb") as f:
        f.write(r.content)


with open(MODEL_FILEPATH, "rb") as f:
    model = pickle.load(f)


@app.route("/", methods=["GET"])
def default():
    return jsonify({"message": "Welcome to the API"})


@app.route("/predict", methods=["POST"])
def predict():
    req_data = ["air_temperature", "pressure", "wind_speed"]

    if not request.json:
        return jsonify({"error": "Request data not found"})

    if not all(k in request.json for k in req_data):
        return jsonify({"error": "Missing required fields"})

    data = [request.json[k] for k in req_data]
    data = np.array(data).reshape(1, -1)
    prediction = model.predict(data)[0]

    return jsonify({"power": prediction})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
