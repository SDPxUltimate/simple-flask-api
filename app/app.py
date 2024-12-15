
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Welcome to our simple flask api"

# your code here
# ...
# your code here

if __name__ == '__main__':
    app.run()
