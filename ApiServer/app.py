import json
import re
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    with open('../generateData/data/dataset.json', 'r') as f:
        d = load_json('../generateData/data/dataset.json')
    
        return jsonify(d)

def load_json(filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            return data

if __name__ =="__main__":
    app.run(host='0.0.0.0', port=5000)

