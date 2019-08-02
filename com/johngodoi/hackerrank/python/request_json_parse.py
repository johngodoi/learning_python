import json
from urllib.request import urlopen


# Complete the function below.
# Base url: https://jsonmock.hackerrank.com/api/movies/search/?Title=

def getMovieTitles(substr):
    return urlopen("http://worldclockapi.com/api/json/est/now")


titles = getMovieTitles("Spiderman")
dict = json.load(titles)
print(dict['$id'])
