from pymongo import MongoClient

# Establish the connection to the MongoClient
connection = MongoClient('localhost', 27017)
# Set to tutorial for testing locally
db = connection['tutorial']
# Set to numbers for testing locally
collection = db['numbers']

'''3 insert operations exist:
    insert_one - inserts one document
    insert_many - inserts multiple documents
    insert - insert single document or array
'''
def insert_doc():
    try:
        id_num = input('Enter ID: ')
        name = input('Enter name: ')
        db.collection.insert(
            {
                "id": id_num,
                "name": name,
            }
        )
        print("Insert was successful \n")
    except Exception as e:
        print("400", str(e))
    return print(True)


insert_doc()


# Reads all the documents in the collection
def read_all_docs():
    try:
        print("Reading all data in Database: \n")
        read_all = collection.find()
        for doc in read_all:
            print(doc)
    except Exception as e:
        print("400", str(e))


# This should take as input a key value pair and find it
def read_one_doc():
    try:
        input_id = input("Enter the ID to look up: ")
        read_one = collection.find({"id": input_id})
        return read_one
    except Exception as e:
        print("400", str(e))


read_one_doc()


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
