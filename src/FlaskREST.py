import json
# needs to not include src to run from command line, needs to include src to run in PyCharm
# from src.Mongo_CRUD import *
from flask import Flask, jsonify

FlaskREST = Flask(__name__)


# Use jsonify to return {hello:"world"}
@app.route("/", methods=['GET'])
def hello():
    return "hello world"


if __name__ == "__main__":
    FlaskREST.run()

'''
command line run:
export FLASK_APP=app.py
Flask run
'''
