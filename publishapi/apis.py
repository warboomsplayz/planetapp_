

import csv
from flask import Flask, jsonify, request
 

app = Flask(__name__)

 
with open('planet_data_.csv', newline="") as f:
  reader = csv.reader(f)
  planet_data = list(reader)
 
with open('terradata.csv', newline="") as f:
  reader = csv.reader(f)
  terra_data = list(reader)
 
 


@app.route("/")
def index():
    return jsonify({
        "data": planet_data,
        "message": "success"
    }), 200

@app.route("/terra")
def terra():
    return jsonify({
        "data": terra_data,
        "message": "success"
    }), 200



if __name__ == "__main__":
    app.run()
