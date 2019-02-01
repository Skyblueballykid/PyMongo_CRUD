from pymongo import MongoClient

# Establish the connection to the MongoClient
connection = MongoClient('localhost', 27017)
# Set to tutorial for testing locally
db = connection['tutorial']
# Set to numbers for testing locally
collection = db['numbers']


def insert_doc():
    try:
        id_num = input('Enter ID: ')
        name = input('Enter name: ')
        db.collection.insert(
            {
                "id": id_num,
                "name": name
            }
        )
        print("Insert was successful \n")
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
    except Exception as e:
        print("400", str(e))


update_doc()


def delete_doc():
    pass
