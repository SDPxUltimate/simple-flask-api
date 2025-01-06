from flask import Flask, jsonify, request
from database import get_all, get_by_id, insert, update, delete
from dotenv import load_dotenv
from utils import convert_users_to_dict, convert_user_to_dict

app = Flask(__name__)

@app.route('/')
def index():
  return "Hello, Welcome to our simple flask api"

@app.route('/user', methods=['GET'])
def get_user():
  try:
    users = get_all('USERS')

    return jsonify(convert_users_to_dict(users))
  except Exception as error:
    return jsonify({"error": str(error)}), 500

@app.route('/user/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
  try:
    user = get_by_id('USERS', user_id)

    if not user:
      return jsonify({"error": "User not found"}), 404

    return jsonify(convert_user_to_dict(user))

  except Exception as error:
    return jsonify({"error": str(error)}), 500

@app.route('/user/new', methods=['POST'])
def create_user():
  try:
    req_body = request.get_json()

    if not req_body or 'name' not in req_body or 'age' not in req_body:
      return jsonify({"error": "Both 'name' and 'age' are required."}), 400

    user_id = insert('USERS', {
      'name': req_body['name'],
      'age': req_body['age'],
    })

    return jsonify({"uid": user_id}), 201

  except Exception as error:
    return jsonify({"error": str(error)}), 500

@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
  try:
    req_body = request.get_json()

    if not req_body or 'name' not in req_body or 'age' not in req_body:
      return jsonify({"error": "Both 'name' and 'age' are required."}), 400

    updated = update('USERS', user_id, {
      'name': req_body['name'],
      'age': req_body['age'],
    })

    if not updated:
      return jsonify({"error": "User not found"}), 404

    return jsonify({"message": f"User with id {user_id} updated successfully"})

  except Exception as error:
    return jsonify({"error": str(error)}), 500

@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
  try:
    deleted = delete('USERS', user_id)

    if not deleted:
      return jsonify({"error": "User not found"}), 404

    return jsonify({"message": f"User with id {user_id} deleted successfully"})

  except Exception as error:
    return jsonify({"error": str(error)}), 500

if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8081)
