import requests
import urllib.request
from datetime import datetime
from bs4 import BeautifulSoup

def get_dia(*args, **kwargs):

    url = "http://www.fundamentus.com.br/detalhes.php?papel=PETR3"
    response = requests.get(url)

    soup = BeautifulSoup(response.content,'html.parser') 
    date = soup.findAll('span')[11].text
    #link = one_a_tag['span']

    return datetime.strptime(date, '%d/%m/%Y')