# MongoDB CRUD application
from pymongo import MongoClient
# TODO: Add prettify module to pretty print json

# Establish the connection to the MongoClient
connection = MongoClient('localhost', 27017)
# Set to city DB
db = connection['city']
# Set to inspections collection
collection = db['inspections']

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
            "business_name": name
        }

        result = db.inspections.insert_one(insertion_doc)

        print(result.inserted_id, '\n', True)

        return (result)

    except Exception as e:
        print("400", str(e), False)


'''
2 read operations exist:
    find() - finds all documents, returns cursor
    find_one() - finds one document, returns object
'''


# Reads all the documents in the collection
def read_all_docs():
    try:
        print("Reading all data in Database: \n")

        read_all = db.inspections.find()

        for doc in read_all:
            print(doc)

    except Exception as e:
        print("400", str(e), False)


# This function takes as input a key-value pair and returns one document
def read_one_doc():
    try:
        input_name = str(input("Enter the name to look up: "))

        read_one = db.inspections.find_one({"business_name": input_name})

        print(read_one)
        # TODO: Pretty print

    except Exception as e:
        print("400", str(e), False)


'''
4 update operations exist:
    update() - returns JSON object
    update_one() - returns UpdateResult object
    update_many() - returns UpdateResult object
    replace_one() - returns UpdateResult object
'''


# This function updates a document
def update_doc():
    try:
        update_id = input("Select ID Number: \n")

        update_name = input("Enter name to update to: \n")

        db.inspections.update_one(

            {"id": update_id},
            {
                "$set": {
                    "business_name": update_name
                }
            }
        )

        print("Document Updated: ", True)

    except Exception as e:
        print("400", str(e), False)


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
            "business_name": delete_name
        }

        db.inspections.delete_one(deletion)

        print("Document Deleted:", True)
    except Exception as e:
        print("400", str(e), False)


# Create the selection menu
def main():
    while True:
        selection = str(input(
            'Select: '
            '\n1 to insert a document '
            '\n2 to read one document '
            '\n3 to read all documents'
            '\n4 to update a document '
            '\n5 to delete a document '
            '\n0 to quit\n\n'))

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


if __name__ == "__main__":
    main()
