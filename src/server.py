from flask import Flask, jsonify
from gen_data import fileloader as fl

app = Flask(__name__)

@app.route('/')
def hello_world():
    f = fl.FileLoader()
    d = f.load_json('./data/dataset.json')
    return jsonify(d)


if __name__ =="__main__":
    app.run()

