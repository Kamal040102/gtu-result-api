from bs4 import BeautifulSoup
import requests

def getResult():
    page = requests.get('https://www.gtu.ac.in/result.aspx').text
    soup = BeautifulSoup(page, 'lxml')
    cards = soup.find_all('div', class_='event-list')
    for card in cards:
        title = card.find('h3', class_='Content').text
        date = card.find('div', class_='date-in').text

        print(f'The {title} has been announced on the date {date}.')