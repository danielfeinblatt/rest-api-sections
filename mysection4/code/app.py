from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose' # this should usually be secured and secret
api = Api(app)

jwt = JWT(app, authenticate, identity)

"""
JWT creates a new end point '/auth'
When we call /auth, we send it a username and password. JWT sends the username and password to the authenticate function. we find the user object and compare the password. if they match, we return the user. the auth endpoint hen returns a jw token. when we send the jw token to the next request we make, jwt uses the indentity function and uses the jw token to get the userid and gets the correct user that the token represents, and if it can do this, then the user in validated
"""

items = []

# All resources must be a class
# With flask_restful, we do not need to use jsonify, as it does it for us. we can just return dictionaries
class Item(Resource):
    # Making the parser a class variable
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be blank"
    )
    # data = request.get_json()
    # to use parser, we replace above line with below line. Since we only defined price in the parser, only the price will be taken and everything else will be ignored

    @jwt_required() # this means we will have to authenticate before we can call the get method
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
        # First deal with errors
        if next(filter(lambda i: i['name'] == name, items), None): # if the item already exists
            return {'message': f'An item with name "{name}" already exists'}, 400 # 400 code mean bad request

        # if no errors, then we can load the data
        data = Item.parser.parse_args()

        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201 # returning item so that the application knows the post was successful. Code 201 is created

    def delete(self, name):
        global items
        items = list(filter(lambda i: i['name'] != name, items)) # setting items to a list that has everything except the item we want to delete
        return {'message': 'Item deleted'}

        # put is an item potent action: we can call the same put request over and over without any change in its result. Put can be used to create an item or update an existing item
    def put(self, name):
        
        data = Item.parser.parse_args()

        item = next(filter(lambda i: i['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        
        return item
            

class ItemList(Resource):
    def get(self):
        return {'items': items}

api.add_resource(Item, '/item/<string:name>') 
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)

