from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.cars.bg/carslist.php?subm=1&add_search=1&typeoffer=1&categoryId=1&conditions%5B%5D=4&conditions%5B%5D=1"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('div', class_='mdc-card offer-item')

with open('cars.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Price']
    thewriter.writerow(header)

    for list in lists:
        title = list.find('h5', class_="card__title mdc-typography "
                                       "mdc-typography--headline5 observable").text.replace('\n', '')
        price = list.find('h6', class_="card__title mdc-typography "
                                       "mdc-typography--headline6 price").text.replace('\n', '')

        info = [title, price]
        thewriter.writerow(info)

