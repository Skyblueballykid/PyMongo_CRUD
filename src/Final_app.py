from bottle import route, run, template, request, abort, response
from pymongo import MongoClient
from bson import json_util
import json
from flask import jsonify
import pprint


# Establish the connection to the MongoClient
connection = MongoClient('localhost', 27017)
# Set to city DB
db = connection['market']
# Set to inspections collection
collection = db['stocks']

# Set the indenting for the PrettyPrinter
pp = pprint.PrettyPrinter(indent=4)


# returns hello + the name (entered after the slash in the URL)
@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


'''
MAIN METHOD FUNCTIONS
'''


# Find a stock by Ticker
def get_stock_main():
    try:
        input_name = str(input("Enter the ticker to look up: "))
        read_one = collection.find_one({"Ticker": input_name})
        if read_one['Ticker'] is None:
            raise ValueError
        else:
            pp.pprint(read_one)

    except Exception as e:
        print("400", str(e), False)


def update_doc_main():
    try:
        input_name = str(input("Enter the ticker to look up: "))
        update_volume = int(input("Enter the new volume: "))

        if int(update_volume) > 0:
            collection.update_one(
                {"Ticker": input_name},
                {
                    "$set": {
                        "Volume": update_volume
                    }
                }
            )
            read_one = collection.find_one({"Ticker": input_name})
            pp.pprint(read_one)

        else:
            print("Volume is less than 1, try again. ")

    except Exception as e:
        print("400", str(e), False)


def delete_doc_main():
    try:
        delete_ticker = input("Enter the ticker of the stock to delete: ")

        deletion = {
            "Ticker": delete_ticker
        }
        collection.delete_one(deletion)

        print("Document Deleted:", True)

    except Exception as e:
        print("400", str(e), False)


# Read (Find one)
# Takes two arguments, numerical low and high values
# returns count of docs between those values
def count_avg_main():
    try:
        input_num1 = float(input("Enter the low number: "))
        input_num2 = float(input("Enter the high number: "))
        if input_num1 > 0.000 and input_num2 < 2.6714 and input_num2 > input_num1:
                print("Low value:", input_num1, ",", "High value: ", input_num2)

        else:
            print("Input range invalid")

    except Exception as e:
        print("400", str(e), False)


# Read (Find one)
# Input string = industry
# returns list of ticker symbols to match that industry
def read_sector_main():
    pass


# Read (Find one)
# Aggregation, multiple pipeline stages
# Input string = sector
# Returns "Total outstanding shares" grouped by Industry
# Create simple main application to call the function
def count_shares_main():
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


# Update a stock using the API
@route('/updateStock', method='PUT')
def update_doc():
    try:
        update_ticker = request.json["Ticker"]
        update_volume = request.json["Volume"]

        if int(update_volume) > 0:
            collection.update_one(
                {"Ticker": update_ticker},
                {
                    "$set": {
                        "Volume": update_volume
                    }
                }
            )

        return_result = collection.find_one({'Ticker': update_ticker})

        output = {"result": return_result}

        return jsonify({'result': output})

    except Exception as e:
        print("400", str(e), False)


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

'''
# Find a stock by name
@route('/getStock', method='GET')
def get_stock():
    data = request.body.readline()
    if not data:
        abort(400, 'No data received')
    entity = json.loads(data)
    if 'Ticker' not in entity:
        abort(400, 'No Ticker specified')
    try:
        return_result = collection.find_one({'Ticker': "AAIT"})
        output = {"result": return_result['result']}
        return jsonify({'result': output})

    except Exception as e:
        abort(400, str(e))
        
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


# Get all stocks
@route('/stocks', method= 'GET')
def get_all_stocks():
    return json.dumps(collection.find().limit(10))


# stockReport
@route('/stockReport/<Ticker>', method='GET')
def stock_report(Ticker):
    try:
        returned_ticker = collection.find_one({'Ticker': Ticker})
        pp.pprint(returned_ticker)
        return json.dumps(returned_ticker, default=json_util.default)
    except Exception as e:
        print("400", str(e), False)


# industryReport
@route('/industryReport/<Industry>', method='GET')
def industry_report(industry):
    pass


# portfolio
@route('/portfolio/<Company>', method='GET')
def portfolio(company):
    pass


# Create the selection menu
def main():
    while True:
        selection = str(input(
            'Select: '
            '\n1 to find a document by ticker symbol'
            '\n2 to update the trading volume'
            '\n3 to delete a stock from the database'
            '\n4 to find the count of documents between a 50-Day Simple Moving Average Range'
            '\n5 to find the list of ticker symbols that match a specified industry'
            '\n6 Enter a sector name to find the total outstanding shares in an industry'
            '\n7 to run the app and access the REST API '
            
            '\n0 to quit\n\n'))

        if selection == '1':
            get_stock_main()
        elif selection == '2':
            update_doc_main()
        elif selection == '3':
            delete_doc_main()
        elif selection == '4':
            count_avg_main()
        elif selection == '5':
            read_sector_main()
        elif selection == '6':
            count_shares_main()
        elif selection == '7':
            run(host='localhost', port=8080)
        elif selection == '0':
            quit()
        else:
            print('\n Selection is Invalid \n')


if __name__ == "__main__":
    main()

