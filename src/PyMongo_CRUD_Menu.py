

while(True):
	selection = input('Select 1 to insert a document \n2 to read a document \n3 to update a document \n4 to delete a document \n0 to quit\n\n')

	if selection == '1':
		insert_doc()
	elif selection == '2':
		read_doc()
	elif selection == '3':
		update_doc()
	elif selection == '4':
		delete_doc()
	elif selection == '0':
		quit()
	else:
		print('\n Selection is Invalid \n')