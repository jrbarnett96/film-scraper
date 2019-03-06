from sklearn import tree
import json
import OmdbScraper
#  decision tree learning

features = [[140, 1], [175, 0],[175, 0]] # all the other data
labels = [0, 1, 3]  # gross income

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

#print(clf.predict([[140,0]]))


with open("items.json") as jsonfile:
    films = []
    #numbers = json.loads(jsonfile.read())
    for line in jsonfile:
        films.append(json.loads(line))

labels.clear()
features.clear()

for movie in films:
    film_dict = OmdbScraper.omdb_data_collector(movie["title"])
    mylist = film_dict[movie["title"]]["Genre"]
    # genre must be numerized
    features.append([movie["worldwide"],movie["domestic"]])
    print(labels)
    print(features)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print(clf.predict([[140,0]]))

