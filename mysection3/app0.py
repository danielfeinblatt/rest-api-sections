from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# POST - used to receive data
# GET - used to send data back only
# These would be seen in reverse from the browser's prospective

# By default, @app.route uses get

# POST /store data: {name:}
@app.route('/store', methods=['POST']) # this makes this route accessible via only a POST request
def create_store():
    request_data = request.get_json() # .get_son() turns the json into a python dictionarys
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>') # <string:name> specifies that the argument to our function is a string called name. This must match in our function definition. Example: 'http://127.0.0.1:500/store/some_name'
def get_store(name):
    # iterate over stores, if the store name matches, return it
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    
    return jsonify({'message': 'store not found'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores}) # jsonify converts the stores variable into json. To convert, it must be a dictionary, so we make the variable into a dictionary

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=["POST"])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    
    return jsonify({'message': 'store not found'})

app.run(port=5000)