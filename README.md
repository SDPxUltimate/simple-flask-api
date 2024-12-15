# simple-flask-api
a simple api using flask, provided 5 end points with RESTful design. 

# install dependencies
- ```pip install flask``` 

# to run the app
1. you must jump into /app folder using ```cd app```
2. run the command ```python app.py```

# 5 endpoints existed
1. GET /user
2. POST /user/new
3. PUT /user/[uid]
4. GET /user/[uid]
5. DELETE /user/[uid]

# user schema
{
  uid: number,
  firstName: string,
  lastName: string,
  nickname: string (max 25 char),
  githubUsername: string,
  age: number (min 0, max 200),
  tools: string[]
}
