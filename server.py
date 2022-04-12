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

@app.route('/new')
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

if __name__=='__main__':
    app.run(debug=True)