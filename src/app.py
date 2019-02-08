from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from pymongo import MongoClient

# Allows for curl like functionality from python interpreter
from requests import get, put


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
        strings = request.form['data']
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
'''


class Create(Resource):
    def post(self):
        try:
            id_num = input('Enter ID: ')
            name = input('Enter name: ')

            insertion_doc = {
                "id": id_num,
                "name": name
            }

            result = db.collection.insert_one(insertion_doc)

            print(result.inserted_id, '\n', True)

        except Exception as e:
            print("400", str(e), False)



'''
"Return the document found with the given business_name"
curl http://localhost:8080/read?business_name="ACME TEST INC."

/read
'''

class Read(Resource):
    def get(self):
        try:
            input_name = str(input("Enter the name to look up: "))

            read_one = db.collection.find_one({"name": input_name})

            return print(read_one)

        except Exception as e:
            print("400", str(e), False)

'''
"Update the result value for the document with the given id string"
curl http://localhost:8080/update?id="10011-2017-TEST"&result="Violation Issued"

/update
'''

class Update(Resource):
    def put(self):
        try:
            update_id = input("Select ID Number: \n")

            update_name = input("Enter name to update: \n")

            db.collection.update_one(

                {"id": update_id},
                {
                    "$set": {
                        "name": update_name
                    }
                }
            )

            print("Document Updated: ", True)

        except Exception as e:
            print("400", str(e), False)

'''
"Delete the document with the given id string"
curl http://localhost:8080/delete?id="10011-2017-TEST"

/delete

'''


class Delete(Resource):
    def delete(self):
        try:
            delete_name = input("Enter the name of the document to delete: ")

            deletion = {
                "name": delete_name
            }

            db.collection.delete_one(deletion)

            print("Document Deleted:", True)
        except Exception as e:
            print("400", str(e), False)


# Support for multiple endpoints
api.add_resource(Hello, '/', '/hello')
api.add_resource(Strings, '/<string:string_id>')
api.add_resource(Create, '/create')
api.add_resource(Read, '/read')
api.add_resource(Update, '/update')
api.add_resource(Delete, '/delete')


if __name__ == "__main__":
    app.run(host='localhost', port='8080', debug=True)



