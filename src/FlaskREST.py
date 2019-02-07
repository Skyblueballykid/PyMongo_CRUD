import json
# needs to not include src to run from command line, needs to include src to run in PyCharm
# from src.Mongo_CRUD import *
from flask import Flask, jsonify

app = Flask(__name__)


# Use jsonify to return {hello:"world"}
@app.route("/", methods=['GET'])
def hello():
    return "hello world"


if __name__ == "__main__":
    app.run()