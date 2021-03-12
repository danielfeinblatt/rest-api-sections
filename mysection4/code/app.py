from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
app.secret_key = 'jose' # this should usually be secured and secret
api = Api(app)

items = []

# All resources must be a class
# With flask_restful, we do not need to use jsonify, as it does it for us. we can just return dictionaries
class Item(Resource):
    def get(self, name):
        # for item in items:
        #     if item['name'] == name:
        #         return item
        # Better way to do this:
        item = next(filter(lambda i: i['name'] == name, items), None)  # Filter returns a filter object, which we can turn into a list (as multiply items may be returned that satisfy the filter)
        # Since we know we have unique names, we can use next() which gives us the next item found by the filter function (which would be the first item). If there are no items and we call next(), we would get an error, so we add the default value None at the second argument
       
        return {'item': item}, 200 if item else 404 # if item uses truthiness, ie if item exists, then use 200.
        # the 404 tells the status code, ie that it was not found. Code 200 means Ok and is most common

    def post(self, name):
        if next(filter(lambda i: i['name'] == name, items), None): # if the item already exists
            return {'message': f'An item with name "{name}" already exists'}, 400 # 400 code mean bad request


        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 # returning item so that the application knows the post was successful. Code 201 is created

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>') 
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)

