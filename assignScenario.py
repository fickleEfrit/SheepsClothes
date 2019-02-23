from flask import Flask
import json
import random

def assignScenario(fileName):
    with open(fileName) as f:
        data = json.load(f)
    rand = random.randint(0, 100)
    sc = data["scenarios"][rand]



def selectWolf(uids):
    rand = random.randint(0, len(uids))





if __name__ == '__main__':
    app.run()