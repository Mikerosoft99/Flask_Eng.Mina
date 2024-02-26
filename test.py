from flask import Flask, request

app=Flask(__name__) #__main__ ==> directly, #file ==> non Direct (import)

users=[
    {
        "id":1,
        "name":"Mina"
    },
    {
        "id":2,
        "name":"Kerollos"
    },
        {
        "id":3,
        "name":"Ahmed"
    },
    {
        "id":4,
        "name":"Noor"
    }
]

@app.route("/") #end_point
def index():
    return "<h1>home page</h1>"
# app.add_url_rule('/', 'index' ,index)

@app.route("/users")
def get_users():
    return users

# http://127.0.0.1:5000/user?name=Mina&age=3&address=Cairo
@app.route("/user")
def get_user():
    # print(dir(request))
    print(request.method) #GET
    print(request.args) # payload # http://127.0.0.1:5000/user?name=Mina&age=3&address=Cairo
    name = request.args.get('name')
    age = request.args.get('age')
    address = request.args.get('address')
    
    return f'user name is {name} and his age is {age} and lives in {address}'

@app.route("/user/<int:id>")
def get_one_user(id):
    # print(dir(request))
    # for user in users:
    #     if user['id']==id:
    #         return user

    x = list(filter(lambda user: user['id']==id, users))[0]
    return x

if __name__ == '__main__':
    app.run(debug=True)