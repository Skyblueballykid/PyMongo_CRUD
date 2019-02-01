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