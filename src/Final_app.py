from bottle import route, run, template, request, abort
from pymongo import MongoClient
import json
from flask import jsonify


# Establish the connection to the MongoClient
connection = MongoClient('localhost', 27017)
# Set to city DB
db = connection['market']
# Set to inspections collection
collection = db['stocks']


# returns hello + the name (entered after the slash in the URL)
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


# Helper function
def insert_doc(document):
    try:
        result = collection.save(document)
    except Exception as e:
        print("400", str(e), False)
    return result


# Create routing for REST API
@route('/createStock', method='POST')
def put_doc():
    data = request.body.readline()
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    if 'Ticker' not in entity:
        abort(400, 'No Ticker specified')
    try:
        insert_doc(entity)
        print(200, "Successfully inserted document.")
    except Exception as e:
        abort(400, str(e))


'''
MAIN METHOD FUNCTIONS
'''


# Find a stock by name
@route('/getStock', method='GET')
def get_stock():
    pass


# Read (Find one)
# Takes two arguments, numerical low and high values
# returns count of docs between those values
@route('/Avg', method='GET')
def count_avg():
    pass


# Read (Find one)
# Input string = industry
# returns list of ticker symbols to match that industry
@route('/Read_Sector', method='GET')
def read_sector():
    pass


# Read (Find one)
# Aggregation, multiple pipeline stages
# Input string = sector
# Returns "Total outstanding shares" grouped by Industry
# Create simple main application to call the function
@route('/Count_shares', method='GET')
def count_shares():
    pass


'''
END MAIN METHOD FUNCTIONS
'''

'''
Update existing documents using appropriate MongoDB statements. 
Specifically, create a function or method in Python or Java that 
will update the document “Volume” key-value pair identified by the string input stock ticker symbol 
“Ticker” and numerical input “Volume” value of your choice greater than zero. 
The function or method will update the document “Volume” key-value pair identified
by the given ticker symbol and a new “Volume” value of your choice greater than zero. 
You will also need to create a simple main application to call your function. 
'''


# Update a stock
@route('/updateStock', method='PUT')
def update_doc():
    pass


'''
Delete existing documents using appropriate MongoDB statements. 
Specifically, create a function or method in Python or Java that will take as input a stock ticker symbol “Ticker.” 
The function or method will remove the document identified by the given ticker symbol. 
For example, use the ticker symbol “BRLI.” 
You will also need to create a simple application scaffold for testing your function or method. 
'''


# Delete a stock
@route('/deleteStock', method='DELETE')
def delete_doc():
    pass


# stockReport
@route('stockReport', method='POST')
def stock_report():
    pass


# industryReport
@route('industryReport/<Industry>', method='GET')
def industry_report():
    pass


# portfolio
@route('portfolio/<Company>', method='GET')
def portfolio():
    pass


# Create the selection menu
def main():
    while True:
        selection = str(input(
            'Select: '
            '\n1 to find a document by ticker symbol'
            '\n2 to find the count of documents between a 50-Day Simple Moving Average Range'
            '\n3 to find the list of ticker symbols that match a specified industry'
            '\n4 Enter a sector name to find the total outstanding shares in an industry'
            '\n5 to run the bottle app and access the REST API '
            '\n0 to quit\n\n'))

        if selection == '1':
            get_stock()
        elif selection == '2':
            count_avg()
        elif selection == '3':
            read_sector()
        elif selection == '4':
            count_shares()
        elif selection == '5':
            run(host='localhost', port=8080)
        elif selection == '0':
            quit()
        else:
            print('\n Selection is Invalid \n')


if __name__ == "__main__":
    main()

