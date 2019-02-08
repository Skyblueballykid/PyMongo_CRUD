from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app2 = Flask(__name__)


app2.config['MONGO_DBNAME'] = 'city'
app2.config['MONGO_URI'] = 'mongodb://localhost:27017/city'

mongo = PyMongo(app2)

# 1.a. Create a basic web service using the RESTful design pattern to implement the following URIs: \
#  http://localhost/hello?name=”world”
# The above URI should return the following JSON-format text: { hello: “world” }

# /, /hello

hello = {"hello": "world"}


@app2.route("/")
def get():
    return jsonify(hello)


# 1.b. HTTP POST the JSON data: {string1:”hello”, string2:”world”} to http://localhost/strings \
# The above URI should return the following JSON-format text:
# { first: “hello”, second: “world” }

# /strings


strings = {}

'''
class Strings(Resource):
    def get(self, string_id):
        return {string_id: strings[string_id]}

    def put(self, string_id):
        strings = request.form['data']
        return {string_id: strings[string_id]}
'''

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


@app2.route("/create", methods=['POST'])
def create():
    inspections = mongo.db.inspections
    try:
        id_num = input('Enter ID: ')
        name = input('Enter name: ')

        insertion_doc = {
            "id": id_num,
            "business_name": name
        }

        result = inspections.insert_one(insertion_doc)

        print(result.inserted_id, '\n', True)

        return jsonify(result)

    except Exception as e:
        print("400", str(e), False)


'''
"Return the document found with the given business_name"
curl http://localhost:8080/read?business_name="ACME TEST INC."

/read
'''


@app2.route("/read", methods=['GET'])
def read(business_name):
    inspections = mongo.db.inspections
    try:
        read_one = inspections.find({"business_name": business_name})

        return jsonify(read_one)

    except Exception as e:
        print("400", str(e), False)


'''
"Update the result value for the document with the given id string"
curl http://localhost:8080/update?id="10011-2017-TEST"&result="Violation Issued"

/update
'''


@app2.route("/update", methods=['PUT'])
def update():
    inspections = mongo.db.inspections
    try:
        update_id = input("Select ID Number: \n")

        update_name = input("Enter name to update to: \n")

        inspections.update_one(

            {"id": update_id},
            {
                "$set": {
                    "business_name": update_name
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


@app2.route("/delete", methods=['DELETE'])
def delete():
    inspections = mongo.db.inspections
    try:
        delete_name = input("Enter the name of the document to delete: ")

        deletion = {
            "business_name": delete_name
        }

        inspections.delete_one(deletion)

        print("Document Deleted:", True)
    except Exception as e:
        print("400", str(e), False)


if __name__ == "__main__":
    app2.run(host='localhost', port='8080', debug=True)
