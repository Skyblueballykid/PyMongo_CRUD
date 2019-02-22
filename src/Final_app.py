from bottle import  route, run, template, request, abort, response
from pymongo import MongoClient
from bson import json_util
from bson.son import SON
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


# Update volume of a stock
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


# delete a stock by Ticker
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
        low_value = float(input("Enter the low number: "))
        high_value = float(input("Enter the high number: "))
        count = 1
        if low_value > 0.000 and high_value < 2.6714 and high_value > low_value:
                print("Low value:", low_value, ",", "High value: ", high_value)
                stocks = collection.find({"50-Day Simple Moving Average": {'$gte': low_value, '$lte': high_value}})
                for s in stocks:
                    tick = s.get("Ticker", "")
                    print("Ticker", count, tick)
                    count += 1
                print("Count", count)
        else:
            print("Input range invalid")

    except Exception as e:
        print("400", str(e), False)


# Read (Find one)
# Input string = industry
# returns list of ticker symbols to match that industry
def read_sector_main():
    industry = input("Enter the name of the industry to look up: ")
    stocks = collection.find({"Industry": industry})
    count = 1
    for s in stocks:
        tick = s.get("Ticker", "")
        print("Ticker", count, tick)
        count += 1


# Read (Find one)
# Aggregation, multiple pipeline stages
# Input string = sector
# Returns "Total outstanding shares" grouped by Industry
# Create simple main application to call the function
def count_shares_main():
    sector = str(input("Enter the name of the Sector to look up: "))
    with connection:
        pipe = [
            {"$match": {"Sector": sector}},
            {"$group": {"_id": "$Industry", "Total Shares": {"$sum": "$Shares Outstanding"}}}
        ]
        agg = list(db.stocks.aggregate(pipe))
        pp.pprint(agg)


'''
END MAIN METHOD FUNCTIONS
'''


'''
API FUNCTIONS
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


# Delete a stock
# Needs to be GET method, not DELETE
@route('/deleteStock/<Ticker>', method='GET')
def delete_doc(Ticker):
    try:
        collection.delete_one({"Ticker": str(Ticker)})

        print("Document Deleted:", True)

    except Exception as e:
        print("400", str(e), False)


# Get all stocks
@route('/stocks', method='GET')
def get_all_stocks():
    output = list()
    stocks = collection.find()
    count = collection.find().count()
    for s in stocks.limit(count):
            try:
                # Error handling in case the key doesn't exist
                tick = s.get("Ticker", "")
                company = s.get("Company", "")
                output.append({"Ticker": tick, 'Company': company})
            except ValueError as e:
                print(e)
    # print the total number of stocks in the collection
    print(len(output))
    return json.dumps(output, default=json_util.default)


# getStock
@route('/getStock/<Ticker>', method='GET')
def get_stock(Ticker):
    try:
        returned_ticker = collection.find_one({'Ticker': Ticker})
        pp.pprint(returned_ticker)
        return json.dumps(returned_ticker, default=json_util.default)
    except Exception as e:
        print("400", str(e), False)


# stockReport
@route('/stockReport', method='POST')
def stock_report():
    try:
        output = list()

        data = request.body.read()
        if not data:
            abort(400, 'No data received')
        # decode the binary data into string
        decoded_data = data.decode('ascii')
        # split the string into a list to pass into the query
        data_list = list(decoded_data.split(' '))
        for _ in data_list:
            stock = collection.find({"Ticker": {"$in": data_list}})
            for s in stock:
                output.append(s)
        pp.pprint(output)
        return json.dumps(output, default=json_util.default)
    except Exception as e:
        print("400", str(e), False)


# industryReport
@route('/industryReport/<industry>', method='GET')
def industry_report(industry):
    try:
        output = list()

        # Mongo cursor object, which is consumed after cycling through it once
        stocks = db.stocks.find({"Industry": str(industry)})

        # Need to append each dict in the cursor to a list of dicts to keep it
        for s in stocks.limit(5):
            output.append(s)

        pp.pprint(output)
        return json.dumps(output, default=json_util.default)

    except Exception as e:
        print("400", str(e), False)


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

