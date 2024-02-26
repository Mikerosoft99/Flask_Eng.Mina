from bson import ObjectId
from flask import Flask, redirect, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/Flask' #created using Robo3T
mongo = PyMongo(app)

# base page
@app.route("/")
def base():
    return render_template('base.html')

# users list page
@app.route("/users")
def get_users():
    users = list(mongo.db.Students.find({}))
    return render_template('users.html', users_html=users)

# delete user ==> redirect to users list after deletion
@app.route("/delete/<string:id>")
def del_user(id):
    mongo.db.Students.delete_one({'_id': ObjectId(id)})
    return redirect('/users')

# update user ==> redirect to users list after updat
@app.route('/update/<string:id>', methods=['GET', 'POST'])
def update_user(id):
    if request.method == 'GET':
        user_to_update = mongo.db.Students.find_one({'_id': ObjectId(id)})
        return render_template('update_user.html', user=user_to_update)
    
    if request.method == 'POST':
        mongo.db.Students.update_one({'_id': ObjectId(id)}, {'$set': {
            'name': request.form['name'],
            'age': request.form['age'],
            'location': request.form['location']
        }})
        return redirect('/users')
    
# create a new user
@app.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return render_template('create_user.html')

    if request.method == 'POST':
        user_data = {
            'name': request.form['name'],
            'age': request.form['age'],
            'location': request.form['location']
        }
        mongo.db.Students.insert_one(user_data)
        return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)