import requests


# 3e6165e0
# http://www.omdbapi.com/?apikey=[yourkey]&
# example usage
# http://www.omdbapi.com/?t=star+wars&apikey=3e6165e0

url = "http://www.omdbapi.com/?t=good+will+hunting&apikey=3e6165e0"


json = requests.get(url).json()
print(json)
