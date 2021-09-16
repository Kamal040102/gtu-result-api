from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route("/")
def getResult():
    page = requests.get('https://www.gtu.ac.in/result.aspx').text
    soup = BeautifulSoup(page, 'lxml')
    cards = soup.find_all('div', class_='event-list')

    result = []
    for card in cards:
        title = card.find('h3', class_='Content').text
        date = card.find('div', class_='date-in').text

        # print(f'The {title} has been announced on the date {date}.')

        result.append(f'The {title} has been announced on date {date}.')

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)