from pymongo import MongoClient

# Establish the connection to the MongoClient
connection = MongoClient('localhost', 27017)
# Set to tutorial for testing locally
db = connection['tutorial']
# Set to numbers for testing locally
collection = db['numbers']


def insert_doc():
    try:
        id_num = input('Enter ID:')
        db.numbers.insert_one(
            {
                "id": id_num
            }
        )
    except Exception as e:
        print("400", str(e))


insert_doc()


def read_doc():
    try:
        print("Reading all data in Database: \n")
        read = collection.find()
        for doc in read:
            print(doc)
    except Exception as e:
        print("400", str(e))


read_doc()


def update_doc():
    pass


def delete_doc():
    pass
