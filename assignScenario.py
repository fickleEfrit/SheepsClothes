import os
from flask import Flask, render_template
from flask_sse import sse
import json
import random

"""
app = Flask(__name__)
app.config["REDIS_URL"] = "redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')
"""

def assignScenario(fileName, uids):
    with open(fileName) as f:
        data = json.load(f)
    randSc = random.randint(0, 100)
    sc = data["scenarios"][randSc]["names"]

    wolfID = selectWolf(uids)

    randH = random.randint(0,5)
    hint = data["scenarios"][randSc]["hints"][randH]
    sse.publish({"user": wolfID, "message": "You are the wolf! Your hint is: " + hint}, type='greeting')
    for x in uids.keys:
        if x == wolfID:
            continue
        else:
            sse.publish({"user": x, "message": "You are a sheep! You are in: " + hint}, type='greeting')



def selectWolf(uids):
    rand = random.randint(0, len(uids))
    wolfId = uids[rand]
    return wolfId

