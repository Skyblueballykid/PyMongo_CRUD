from bottle import route, run, template, request, abort
from pymongo import MongoClient
import json
from flask import jsonify


# Establish the connection to the MongoClient
connection = MongoClient('localhost', 27017)
# Set to city DB
db = connection['market']
# Set to inspections collection
collection = db['stocks']


# returns hello + the name (entered after the slash in the URL)
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


def insert_doc(document):
    try:
        result = collection.save(document)
    except Exception as e:
        print("400", str(e), False)
    return result


@route('/create', method='POST')
def put_document():
    data = request.body.readline()
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    if 'Ticker' not in entity:
        abort(400, 'No Ticker specified')
    try:
        insert_doc(entity)
        print(200, "Successfully inserted document.")
    except Exception as e:
        abort(400, str(e))


run(host='localhost', port=8080)