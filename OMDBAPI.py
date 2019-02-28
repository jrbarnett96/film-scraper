import requests
import sys

# baseurl = "http://www.omdbapi.com/?t={}&apikey=3e6165e0"
# conner_api_key  = 3e6165e0
# http://www.omdbapi.com/?apikey=[api_key]&
# example usage
# http://www.omdbapi.com/?t=star+wars&apikey=3e6165e0

'''
Searches for FILMS in FILM_LIST using the OMDB API, given an API key. When a film is found, 
downloads its JSON file and enters it into a dictionary indexed by film name. Prints the 
contents of the dictionary.
'''


def omdb_data_collector(film_list, api_key):

    """ Replace the API field with api_key. """
    url = "http://www.omdbapi.com/?t={}&apikey={}"
    url = url.format('{}', api_key)

    film_dict = {}

    """ For each film in film_list, download its JSON file and place it in a dictionary. """
    for film in film_list:

        url = url.format("+".join(film.split()))
        json = requests.get(url).json()
        film_dict[film] = json

        # ~~~~financial data scraping~~~~~
        # insert FINANCIAL DATA as dict keys ('Budget', 'Domestic', etc)
        # There is already a key called 'BoxOffice' with value 'N/A'

    """ Print all keys and associated JSON files in film_dict. """
    for elems in film_dict:
        print(elems, film_dict[elems])


if __name__ == "__main__":

    key = input("Please input your OMDB API key:")
    films = input("Please input desired films in the following format")
    key = sys.argv[2]
    omdb_data_collector(films, key)


