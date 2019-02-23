import os
from flask import Flask, render_template
from flask_sse import sse
import json
import random

app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/hello')
def publish_hello():
    sse.publish({"message": "Hello!"}, type='greeting')
    return "Message sent!"

def assignScenario(fileName, uids):
    with open(fileName) as f:
        data = json.load(f)
    randSc = random.randint(0, 100)
    sc = data["scenarios"][randSc]["names"]

    wolfID = selectWolf(uids)

    randH = random.randint(0,5)
    hint = data["scenarios"][randSc]["hints"][randH]

    sse.publish({"active_users": 100}, channel="analytics")
    sse.publish({"user": "alice", "status": "Life is good!"}, channel="users.social")




def selectWolf(uids):
    rand = random.randint(0, len(uids))
    wolfId = uids[rand]
    return wolfId

