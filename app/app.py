
from flask import Flask, json, jsonify

app = Flask(__name__)

def getUsersFromDB():
  with open("./users.json", encoding="utf-8") as json_file:
      parsed_json = json.load(json_file)
      return parsed_json
    
@app.route('/')
def index():
    return "Hello, Welcome to our simple flask api"

@app.route('/user', methods=['GET'])
def getUser():
  user = getUsersFromDB()
  return jsonify(user)

# your code here
# ...
# your code here

if __name__ == '__main__':
    app.run()
