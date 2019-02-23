from flask import Flask
from flask import request
from flask import render_template
from flask_sse import sse
from flask import session
from flask import redirect
from flask import url_for
import json
import random

app = Flask(__name__)

users = []
roles = {}

game_in_progress = False


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/add_user', methods=['POST'])
def add_user(): #add user to our list of users from submitted
    data = request.form
    users.append(data['username'])
    session['username'] = data['username']
    return redirect(url_for('lobby'))


@app.route('/lobby', methods=['GET'])
def lobby():
    return render_template('lobby.html', users=users)


def assignRoles():
    wolfID = selectWolf(users)
    for x in users:
        if x == wolfID:
            roles[x] = 'wolf'
        else:
            roles[x] = 'sheep'



def selectWolf(uids):
    rand = random.randint(0, len(uids))
    wolfId = uids[rand]
    return wolfId


if __name__ == '__main__':
    app.run()
