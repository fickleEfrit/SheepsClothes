from flask import Flask
import json
from pprint import pprint

with open('data.json') as f:
    data = json.load(f)

pprint(data)

@app.route('/')

def assignScenario(fileName):


def selectWolf():




if __name__ == '__main__':
    app.run()