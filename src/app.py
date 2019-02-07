from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient

# Allows for curl like functionality from python interpreter
from requests import get, put

from src.Mongo_CRUD import *

app = Flask(__name__)
api = Api(app)

# Establish the connection to the MongoClient
connection = MongoClient('localhost', 27017)
# Set to tutorial for testing locally
db = connection['tutorial']
# Set to numbers for testing locally
collection = db['numbers']


# 1.a. Create a basic web service using the RESTful design pattern to implement the following URIs: \
#  http://localhost/hello?name=”world”
# The above URI should return the following JSON-format text: { hello: “world” }

# /, /hello

hello = {"hello": "world"}


class Hello(Resource):
    def get(self):
        return jsonify(hello)


# 1.b. HTTP POST the JSON data: {string1:”hello”, string2:”world”} to http://localhost/strings \
# The above URI should return the following JSON-format text:
# { first: “hello”, second: “world” }

# /strings


strings = {}


class Strings(Resource):
    def get(self, string_id):
        return {string_id: strings[string_id]}

    def put(self, string_id):
        strings[string_id] = request.form['data']
        return {string_id: strings[string_id]}


# put('http://127.0.0.1:5000/string', data={'first': "hello"})
# put('http://127.0.0.1:5000/string', data={'second': "world"})



# 2. Using the RESTful web service you created in Step 1, add URI paths to the RESTful service \
# for each of your CRUD functions completed in Milestone One. Your URI paths should be able to \
# handle the following curl client interactions:

'''
"Add the following document to the collection:"
curl -H "Content-Type: application/json" -X POST -d ' \
{"id" : "10011-2017-TEST","certificate_number" : 9278833,"business_name" : “ACME TEST INC.", \
"date" : "Feb 20 2017","result" : "No Violation Issued","sector" : "Test Retail Dealer - 101"}' \
http://localhost:8080/create

/create

"Return the document found with the given business_name"
curl http://localhost:8080/read?business_name="ACME TEST INC."

/read

"Update the result value for the document with the given id string"
curl http://localhost:8080/update?id="10011-2017-TEST"&result="Violation Issued"

/update

"Delete the document with the given id string"
curl http://localhost:8080/delete?id="10011-2017-TEST"

/delete

'''

# Support for multiple endpoints
api.add_resource(Hello, '/', '/hello')

api.add_resource(Strings, '/<string:string_id>')

'''
api.add_resource(Create, '/Create')
api.add_resource(Read, '/Read')
api.add_resource(Update, '/Update')
api.add_resource(Delete, '/Delete')
'''

if __name__ == "__main__":
    app.run(host='localhost', port='8080', debug=True)



