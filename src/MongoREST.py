# importing the Mongo_CRUD file is not working when running this script from the command line
from flask import Flask, jsonify

app = Flask(__name__)

# Use jsonify to return {hello:"world"}
@app.route("/", methods=['GET'])
def hello():
    return "hello world"


if __name__ == "__main__":
    app.run()

