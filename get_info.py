import requests
from bs4 import BeautifulSoup


def info():
    url = 'http://rostovmeteo.ru'
    response = requests.get(url=url).text
    soup = BeautifulSoup(response, "lxml")
    res = soup.find(id='table').find_all('td')
    return f'{res[0].text}\n{res[9].text}  {res[10].text}\n{res[19].text}  {res[20].text}'
