import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time


def weather():
    url = 'http://rostovmeteo.ru'
    response = requests.get(url=url).text
    soup = BeautifulSoup(response, "lxml")
    data = soup.find(id='table').find_all('td')
    result = list()
    for i in range(0, len(data), 2):
        if 'декабря' in data[i].text or 'января' in data[i].text or \
           'утро' in data[i].text or 'ночь' in data[i].text or \
           'день' in data[i].text or 'вечер' in data[i].text or '...' in data[i].text:
            if len(data[i].text) < 15:
                result.append(f'\n {data[i - 1].text:<10} {data[i].text:<30}')
            else:
                result.append('\n\n' + data[i].text)
    return ' '.join(result)


def news_itproger():
    driver = webdriver.Edge()
    url = 'https://itproger.com/news'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "lxml")
    data = soup.find_all(class_='article')
    result = list()
    [result.append('\n\n' + i.find('a').get('title') +
                   '\n\n' + i.a.next_sibling.next_sibling.next_sibling.text +
                   '\n' + 'itproger.com/' + i.find('a').get('href') +
                   '\n' + '_' * 70) for i in data]
    time.sleep(1)
    driver.quit()
    return ' '.join(result)

