from pymongo import MongoClient



# Establish the connection to the MongoClient
connection = MongoClient('localhost',27017)
# Set to tutorial for testing locally
db = connection['tutorial']
# Set to numbers for testing locally
collection = db['numbers']

print(collection)


def insert():
    try:
        id = input('Enter ID:')
    except IOError as ioe:
        print("400", str(ioe))
    return id


insert()


def insert_doc(document):
    try:
        inserted_doc = collection.save(document)
    except ValueError as ve:
        print("400", str(ve))
    return insert_doc


def read_doc():
    try:
        print("Reading all data in Database: \n")
        read = collection.find()
        for doc in read:
            print(doc)
    except ValueError as ve:
        print("400", str(ve))
    return read


def update_doc():
    return


def delete_doc():
    return
