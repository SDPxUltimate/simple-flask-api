def convert_users_to_dict(users):
  return [
    convert_user_to_dict(user)
    for user in users
  ]

def convert_user_to_dict(user):
  return {
    "uid": user[0], 
    "name": user[1], 
    "age": user[2]
  }