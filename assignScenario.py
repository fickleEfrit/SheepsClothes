import json
import random

fileName = "C:\\" + "Users\Justin\PycharmProjects\SheepsClothes\word_bank.json"
sc = None
hint = None

def assignScenario(uids):
    with open(fileName) as f:
        data = json.load(f)
    randSc = random.randint(0, 40)
    sc = data['wordbank'][randSc]['tword']

    wolfID = selectWolf(uids)

    randH = random.randint(0,3)
    hint = data['wordbank'][randSc]['words'][randH]
    for x in uids.keys:
        if x == wolfID:
            continue
        else:
            #help
            continue


def selectWolf(uids):
    rand = random.randint(0, len(uids))
    wolfId = uids[rand]
    return wolfId

def getHint():
    return hint

def getScenario():
    return sc


