import time

from bs4 import BeautifulSoup
import requests
def find_cars():
    html_text = requests.get("https://www.cars.bg/carslist.php?subm=1&add_search=1&typeoffer=1&brandId=69&models%5B%5D=1230&conditions%5B%5D=4&conditions%5B%5D=1").text
    soup = BeautifulSoup(html_text, 'lxml')
    cars = soup.find_all('div', class_="mdc-card offer-item")
    for car in cars:
        car_name = car.find('h5', class_="card__title mdc-typography mdc-typography--headline5 observable").text.replace(' ', '')
        city_name = car.find('div', class_= "card__footer mdc-typography mdc-typography--body2 align-bottom").text.replace(' ','')
        price = car.find('h6', class_ = "card__title mdc-typography mdc-typography--headline6 price").text.replace(' ','')
        published = car.find('h6', class_="card__subtitle mdc-typography mdc-typography--overline").text.replace(' ','')
        print(f'Car Name: {car_name.strip()}')
        print(f'City Name: {city_name.strip()}')
        print(f'Car Price: {price.strip()}')
        print(f'Published: {published.strip()} \n')

if __name__ == '__main__':
    while True:
        find_cars()
        time_wait = 5
        print(f'Waiting {time_wait} minutes for the next search...')
        time.sleep(time_wait * 60)