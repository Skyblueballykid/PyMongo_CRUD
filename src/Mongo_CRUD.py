import pymongo
from pymongo import MongoClient
import json
from bson import json_util


# Establish the connection to the MongoClient
connection = MongoClient('localhost',27017)
# Set to tutorial for testing locally
db = connection['tutorial']
# Set to numbers for testing locally
collection = db['numbers']


print(collection)


def insert_doc(document):
	try:
		insert = collection.save(document)
	except ValidationError as ve:
		abort(400, str(ve))
	return insert

def read_doc():
	try:
		read = collection.find()
		for doc in read:
			print(doc)
	except ValidationError as ve:
		abort(400, str(ve))
	return read

