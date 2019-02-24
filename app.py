from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect
from flask import url_for
from random import randint

app = Flask(__name__)
app.secret_key = 'smklADSF,l32'
users = []
roles = {}

game_in_progress = False


def assignRoles():
   wolfID = selectWolf(users)
   for x in users:
       if x == wolfID:
           roles[x] = 'wolf'
       else:
           roles[x] = 'sheep'


def selectWolf(uids):
   rand = randint(0, len(uids) - 1)
   wolfId = uids[rand]
   return wolfId



@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/add_user', methods=['POST'])
def add_user(): #add user to our list of users from submitted
    data = request.form
    cur_user = data['username']
    users.append(cur_user)
    session['username'] = cur_user
    return redirect(url_for('lobby'))


@app.route('/lobby', methods=['GET'])
def lobby():
    if game_in_progress:
        return redirect(url_for('game'))
    else:
        return render_template('lobby.html', users=users)


@app.route('/game', methods=['GET'])
def game():
    print(session)
    print(roles)
    return render_template('game.html', roles=roles)


@app.route('/start_game', methods=['POST'])
def start_game():
    assignRoles()
    game_in_progress = True
    return redirect(url_for('game'))


if __name__ == '__main__':
    app.run()
