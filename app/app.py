
from flask import Flask, json, jsonify, request


app = Flask(__name__)

@app.route('/guide', methods=["POST"])
def add_guide():
    title = request.json['title']

def getUsersFromDB():
  with open("./users.json", encoding="utf-8") as json_file:
      parsed_json = json.load(json_file)
      return parsed_json

def writeUserstoDB(Json_data):
  with open("./users.json", "w") as json_file:
    json.dump(Json_data, json_file, indent=2)

def generateUID():
  users = getUsersFromDB()
  last_uid = users[-1]['uid']
  uid = str(int(last_uid) + 1)
  return uid
    
@app.route('/')
def index():
    return "Hello, Welcome to our simple flask api"

@app.route('/user', methods=['GET'])
def getUser():
  users = getUsersFromDB()
  return jsonify(users)

@app.route('/user/new', methods=['POST'])
def postUser():
  new_user = request.get_json()
  # user must not have own uid
  if 'uid' in new_user:
    return False
  # check required field
  if ( not (new_user['firstName'] and new_user['lastName'] and new_user['nickName'])):
    return False
  # check nickName length
  if len(new_user['nickName']) > 25:
    return False
  # check if github is null:
  if ('githubUsername' not in new_user) or (not new_user['githubUsername']):
    new_user['githubUsername'] = None
  # check age interval
  if not (type(new_user['age']) is int and 0 <= new_user['age'] <= 200 ):
    return False
  # check valid type of tools, if null replace with []
  if 'tools' not in new_user:
    new_user['tools'] = []
  elif type(new_user['tools'] is not list(str)):
    return False
  # insert uid key to the last
  new_user['uid'] = generateUID()
  users = getUsersFromDB()
  users.append(new_user)
  writeUserstoDB(users)
  return jsonify(users)

# your code here
# ...
# your code here

if __name__ == '__main__':
    app.run()
