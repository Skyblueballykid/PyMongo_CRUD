# needs to not include src to run from command line, needs to include src to run in PyCharm
# from Mongo_CRUD import *
from flask_api import FlaskAPI


app = FlaskAPI(__name__)


# Use jsonify to return {hello:"world"}
@app.route("/", methods=['GET'])
def hello():
    return {'hello': 'world'}

# 1.a. Create a basic web service using the RESTful design pattern to implement the following URIs: \
#  http://localhost/hello?name=”world”
# The above URI should return the following JSON-format text: { hello: “world” }


# 1.b. HTTP POST the JSON data: {string1:”hello”, string2:”world”} to http://localhost/strings \
# The above URI should return the following JSON-format text:
# { first: “hello”, second: “world” }


# 2. Using the RESTful web service you created in Step 1, add URI paths to the RESTful service \
# for each of your CRUD functions completed in Milestone One. Your URI paths should be able to \
# handle the following curl client interactions:

'''
"Add the following document to the collection:"
curl -H "Content-Type: application/json" -X POST -d ' \
{"id" : "10011-2017-TEST","certificate_number" : 9278833,"business_name" : “ACME TEST INC.", \
"date" : "Feb 20 2017","result" : "No Violation Issued","sector" : "Test Retail Dealer - 101"}' \
http://localhost:8080/create

"Return the document found with the given business_name"
curl http://localhost:8080/read?business_name="ACME TEST INC."

"Update the result value for the document with the given id string"
curl http://localhost:8080/update?id="10011-2017-TEST"&result="Violation Issued"

"Delete the document with the given id string"
curl http://localhost:8080/delete?id="10011-2017-TEST"

'''


if __name__ == "__main__":
    app.run()

