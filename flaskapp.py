from flask import Flask, redirect,render_template, request, url_for

app = Flask(__name__)
users = [
    {
        'id': 1,
        'Name': 'Kerollos',
        'Age': 24,
        'Location': 'Minia'
    },
    {
        'id': 2,
        'Name': 'Ahmed',
        'Age': 31,
        'Location': 'Cairo'
    },
    {
        'id': 3,
        'Name': 'John',
        'Age': 28,
        'Location': 'Alexandria'
    },
    {
        'id': 4,
        'Name': 'Emma',
        'Age': 27,
        'Location': 'Luxor'
    },
    {
        'id': 5,
        'Name': 'Jenny',
        'Age': 29,
        'Location': 'Aswan'
    }
]

def get_next_id():
    if len(users) > 0:
        return users[-1]['id'] + 1
    else:
        return 1 # first id

# base page
@app.route("/")
def index():
    return render_template('base.html')

# users list page
@app.route("/users")
def get_users():
    name = request.args.get('Name')
    age = request.args.get('Age')
    location = request.args.get('Location')
    if name !=None or age != None or location !=None :
        users.append({
            'id':get_next_id(),
            "Name":name,
            'Age':age,
            'Location':location
        })
    print(users)
    return render_template('users.html',users_html=users)

# delete user ==> redirect to users list after deletion
@app.route("/delete/<int:id>")
def del_user(id):
    if id is not None and len(users) != 0:
        # for i in range(len(users)):
        #     if users[i]['id']==id:
        #         del users[i]
        #         print(f'deleted {users[i]}')
        #         break
        for user in users:
            if user['id'] == id:
                users.remove(user)
                break
    return redirect('/users')

# edit page (update form)
@app.route('/edit/<int:id>')
def edit_user(id):
    if id is not None and len(users) != 0:
        for user in users:
            if user['id'] == id:
                user_to_edit = user
                break
    return render_template('edit_user.html', user=user_to_edit)

# update user ==> redirect to users list after updating
@app.route('/update/<int:id>', methods=['POST'])
def update_user(id):
    if id is not None and len(users) != 0:
        for user in users:
            if user['id'] == id:
                user['Name'] = request.form['name']
                user['Age'] = request.form['age']
                user['Location'] = request.form['location']
                break
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)