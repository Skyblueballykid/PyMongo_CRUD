from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.son import SON

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
    def get(self, string_id):
        return {string_id: strings[string_id]}
'''


@app2.route("/strings", methods=['POST'])
def add_string():
    inspections = mongo.db.inspections

    try:

        string1 = request.json['string1']
        string2 = request.json['string2']

        inspect_result = inspections.insert({"string1": string1, "string2": string2})
        return_result = inspections.find_one({"_id": inspect_result})

        output = {'first': return_result['string1'], 'second': return_result['string2']}

        return jsonify({'result': output})

    except Exception as e:
        print("400", str(e), False)

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

        company_id = request.json['id']
        certificate_number = request.json['certificate_number']
        business_name = request.json['business_name']
        date = request.json['date']
        result = request.json['result']
        sector = request.json['sector']

        company = inspections.insert({
            "id": company_id,
            "certificate_number": certificate_number,
            "business_name": business_name,
            "date": date,
            "result": result,
            "sector": sector
        })

        return_result = inspections.find_one({"_id": company})

        output = {'id': return_result['id'],
                  'certificate_number': return_result['certificate_number'],
                  'business_name': return_result['business_name'],
                  'date': return_result['date'],
                  'result': return_result['result'],
                  'sector': return_result['sector']}

        return jsonify({'result': output})

    except Exception as e:
        print("400", str(e), False)


'''
"Return the document found with the given business_name"
curl http://localhost:8080/read?business_name="ACME TEST INC."

/read
'''


# Read all
@app2.route("/reads", methods=['GET'])
def read_all():

    inspections = mongo.db.inspections

    try:
        all_inspect = inspections.find()
        return dumps(all_inspect)

    except Exception as e:
        print("400", str(e), False)


# Read one
@app2.route("/read", methods=['GET', 'POST'])
def read():

    inspections = mongo.db.inspections

    business_name = request.json['business_name']

    try:

        query = {"business_name": business_name}

        read_one = inspections.find_one(query)
        output = {"business_name": read_one['business_name']}

        return jsonify({'result': output})

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
        update_id = request.json["id"]

        result = request.json["result"]

        inspections.update_one(

            {"id": update_id},
            {
                "$set": {
                    "result": result
                }
            }
        )

        return_result = inspections.find_one({'id': update_id})

        output = {"result": return_result['result']}

        return jsonify({'result': output})

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

        delete_id = request.json['id']

        inspections.remove({"id": delete_id})

        return "", 200

    except Exception as e:
        print("400", str(e), False)


if __name__ == "__main__":
    app2.run(host='localhost', port='8080')
