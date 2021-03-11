from flask import Flask

app = Flask(__name__)

# Need to tell the app what requests it needs to understand
@app.route('/') # telling our app what it needs to understand, website ending in a '/' (all websites have this trailing slash, just browsers usually hide or remove it)
def home():
    # Need to return a response so that the browser can receive something back to show on the website
    return "Hello, world!"

# Tell our app to run and given port
app.run(port=5000)

# To run this, we type 'python app.py' in the terminal