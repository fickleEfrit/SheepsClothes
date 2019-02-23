from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect
from flask import url_for

app = Flask(__name__)
app.secret_key = 'smklADSF,l32'
users = []
roles = {}

game_in_progress = False


@app.route('/', methods=['GET'])
def hello_world():
    return render_template('index.html')


@app.route('/add_user', methods=['POST'])
def add_user(): #add user to our list of users from submitted
    data = request.form
    cur_user = data['username']
    users.append(cur_user)
    session['username'] = cur_user
    roles[cur_user] = 'wolf'
    return redirect(url_for('lobby'))


@app.route('/lobby', methods=['GET'])
def lobby():
    return render_template('lobby.html', users=users)


@app.route('/game', methods=['GET'])
def game():
    print(session)
    print(roles)
    return render_template('game.html', roles=roles)


if __name__ == '__main__':
    app.run()
