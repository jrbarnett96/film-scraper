import requests
import json


def omdb_data_collector(film_list=("good will hunting"), api_key="3e6165e0"):
    """ Return a mapping of films in FILM_LIST to jsons gathered from OMDB's API with API_KEY. """


    """ Replace the API field with api_key. """
    url = "http://www.omdbapi.com/?t={}&apikey={}"
    url = url.format('{}', api_key)

    film_dict = {}

    """ For each film in film_list, download its JSON file and place it in a dictionary. """
    for film in film_list:

        url = url.format("+".join(film.split()))
        omdb_json = requests.get(url).json()
        film_dict[film] = omdb_json

    return film_dict


def film_list_saver(film_dict):
    for film in film_dict.keys():
        json_dict = film_dict[film]
        film_name = "_".join(film.split())
        json_saver(film_name, json_dict)


def json_saver(name, json_dict):
    """ Create a json file from JSON_DICT and save it to current directory with name NAME"""

    """ Write json_dict to a json file. """
    json_from_dict = json.dumps(json_dict)

    """ Open a file in write mode. """
    json_file = open(name + ".json", 'w')

    """ Write json file to file and close it. """
    json_file.write(json_from_dict)
    json_file.close()

    return json_file


if __name__ == "__main__":
    print(omdb_data_collector())