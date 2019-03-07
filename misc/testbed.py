from sklearn import tree
import json
import OmdbScraper
#  decision tree learning


def convert_genres_to_numeral(mylist, genreset): # needs work

    for elem in mylist:
        if elem in mylist:
            #if elem != "N/A":
            genreset.append(elem)
    numeral = genreset.index(mylist[-1])
    print(genreset)
    return numeral, genreset


with open("items.json") as jsonfile:
    films = []
    for line in jsonfile:
        films.append(json.loads(line))

labels = []
features = []
genreset = []

for movie in films:
    film_dict = OmdbScraper.omdb_data_collector(movie["title"])
    if "Genre" in film_dict[movie["title"]].keys():
        mylist = list(film_dict[movie["title"]]["Genre"].replace(",", "").split())
        genre,genreset = convert_genres_to_numeral(mylist,genreset)
        if genre != "N/A":
            labels.append(genre)
            features.append([int(movie["worldwide"][1:-2].replace(',','')),
                         int(movie["domestic"][1:-2].replace(',',''))])
            print(labels)
            print(features)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print(clf.predict([[1000000000,200000000]]))

