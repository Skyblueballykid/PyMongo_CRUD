from pymongo import MongoClient
from pprint import pprint

# Establish the connection to the MongoClient
connection = MongoClient('localhost', 27017)
# Set to tutorial for testing locally
db = connection['tutorial']
# Set to numbers for testing locally
collection = db['numbers']


'''
3 insert operations exist:
    insert_one - inserts one document
    insert_many - inserts multiple documents
    insert - insert single document or array
'''


def insert_doc():
    try:
        id_num = input('Enter ID: ')
        name = input('Enter name: ')
        db.collection.insert_one(
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

'''
2 read operations exist:
    find() - finds all documents
    find_one() - finds one document
'''


# Reads all the documents in the collection
def read_all_docs():
    try:
        print("Reading all data in Database: \n")
        read_all = collection.find()
        for doc in read_all:
            print(doc)
    except Exception as e:
        print("400", str(e))


# This function takes as input a key value pair and return one document
def read_one_doc():
    try:
        input_name = input("Enter the name to look up: ")
        read_one = collection.find_one({"name": input_name})
        return print(read_one)
    except Exception as e:
        print("400", str(e))


read_one_doc()


'''
4 update operations exist:
    update()
    update_one()
    update_many()
    replace_one()
'''


# This function updates a document
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

'''
2 delete operations exist:
    delete_one()
    delete_many()
Both methods return a DeleteResult object
'''


# This function deletes a document
def delete_doc():
    
    pass
