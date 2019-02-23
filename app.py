from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
users = []
user_sessions = [] #key -- user's name, val -- user_session

@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/add_user', methods=['POST'])
def add_user(): #add user to our list of users from submitted
    data = request.form
    users.append(data['username'])
    return render_template('lobby.html', users=users)


if __name__ == '__main__':
    app.run()
