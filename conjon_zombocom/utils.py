import os

""" Sets the destination file for FilmSpider. """
def set_feed_uri():
    while True:
        filename = input('Please enter a valid filename: ')
        if os.path.isfile('./data/' + filename):
            print('File already exists, please try again.')
        else:

    return


""" Creates a folder for data, if not already present. """
def create_data_folder():
    if os.path.isdir('./data'):
        return
    else:
        os.mkdir('./data')
        return
