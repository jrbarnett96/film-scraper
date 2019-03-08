import json


def readjson(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(json.loads(line))

    for elements in data:
        yield elements


for i in readjson("films.json"):
    print(i)
