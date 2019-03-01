import requests
import BeautifulSoup

html = requests.get('my_url').content

def get_tables(htmldoc):
    soup = BeautifulSoup.BeautifulSoup(htmldoc)
    return soup.findAll('table')

