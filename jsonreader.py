import json

import json

data = []
with open('films.json') as f:
    for line in f:
        data.append(json.loads(line))

for elements in data:
    print(elements)