from pymongo import MongoClient

# Establish the connection to the MongoClient
connection = MongoClient('localhost', 27017)
# Set to tutorial for testing locally
db = connection['tutorial']
# Set to numbers for testing locally
collection = db['numbers']


'''
3 insert operations exist:
    insert_one - inserts one document, InsertOneResult object
    insert_many - inserts multiple documents, InsertManyResult object
    insert - insert single document or array, returns ObjectID of inserted documents
'''


def insert_doc():
    try:
        id_num = input('Enter ID: ')
        name = input('Enter name: ')

        insertion_doc = {
            "id": id_num,
            "name": name
        }

        result = db.collection.insert_one(insertion_doc)

        print(result.inserted_id, '\n', True)

    except Exception as e:
        print("400", str(e))


'''
2 read operations exist:
    find() - finds all documents, returns cursor
    find_one() - finds one document, returns object
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


# This function takes as input a key-value pair and returns one document
def read_one_doc():
    try:
        input_name = str(input("Enter the name to look up: "))

        read_one = db.collection.find_one({"name": input_name})

        return print(read_one)

    except Exception as e:
        print("400", str(e))


'''
4 update operations exist:
    update() - returns JSON object
    update_one() - returns UpdateResult object
    update_many() - returns UpdateResult object
    replace_one() - returns UpdateResult object
'''


# This function updates a document
#TODO: Need to improve this function
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

        print("Document Updated: ", True)

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
    try:
        delete_name = input("Enter the name of the document to delete: ")

        deletion = {
            "name": delete_name
        }

        db.collection.delete_one(deletion)

        print("Document Deleted:", True)
    except Exception as e:
        print("400", str(e))


# Create the selection menu
def main():
    while True:
        selection = input(
            'Select: '
            '\n1 to insert a document '
            '\n2 to read one document '
            '\n3 to read all documents'
            '\n4 to update a document '
            '\n5 to delete a document '
            '\n0 to quit\n\n')

        if selection == '1':
            insert_doc()
        elif selection == '2':
            read_one_doc()
        elif selection == '3':
            read_all_docs()
        elif selection == '4':
            update_doc()
        elif selection == '5':
            delete_doc()
        elif selection == '0':
            quit()
        else:
            print('\n Selection is Invalid \n')


main()
