from flask import Flask, render_template, request, redirect, session
from users import User
app = Flask(__name__)
app.secret_key = 'shbequietimmakey'

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    users = User.get_all()
    print(users)
    return render_template('index.html', users = users)

@app.route('/users/new')
def new():
    return render_template('users.html')

@app.route('/create', methods=["POST"])
def create():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect('/users')

@app.route('/users/<user_id>')
def profile(user_id):
    users = User.get_all()
    for user in users:
        if str(user.id) == str(user_id):
            target_user = user
            break
    return render_template('profile.html', user = target_user)

@app.route('/users/<user_id>/edit')
def edit(user_id):
    users = User.get_all()
    for user in users:
        if str(user.id) == str(user_id):
            target_user = user
            break
    
    return render_template('edit.html', user = target_user)

@app.route('/users/update', methods=["POST"])
def update():
    data = {
        "id": request.form['which_user'],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.update(data)

    return redirect("/users")

@app.route('/users/<user_id>/delete')
def delete_confirm(user_id):
    users = User.get_all()
    for user in users:
        if str(user.id) == str(user_id):
            target_user = user
            break

    return render_template('delete.html', user = target_user)

@app.route('/delete', methods=["POST"])
def delete_user():
    if request.form['confirm'] == 'yes':
        data = {
            "id": request.form['which_user']
        }
        User.delete(data)
        return redirect('/users')
    else:
        return redirect('/users')



if __name__=='__main__':
    app.run(debug=True)