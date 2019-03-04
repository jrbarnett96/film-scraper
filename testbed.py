from sklearn import tree

#  decision tree learning

features = [[140, 1], [175, 0]] # all the other data
labels = [0, 1, 3]  # gross income

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print(clf.predict([[140,0]]))
