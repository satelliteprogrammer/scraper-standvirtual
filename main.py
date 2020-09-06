# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright 2020  Luis Murta

import requests
from bs4 import BeautifulSoup
from math import ceil

months = dict(Janeiro='Jan', Fevereiro='Feb', Março='Mar', Abril='Apr', Maio='May', Junho='Jun', Julho='Jul',
              Agosto='Aug', Setembro='Sep', Outubro='Oct', Novembro='Nov', Dezembro='Dec')

base_url = 'https://www.standvirtual.com/carros/'

search_filter = '?search[filter_enum_fuel_type]=gaz' \
                '&search[filter_enum_gearbox_type][0]=manual' \
                '&search[filter_enum_number_doors][0]=5'


def search(query):
    response = requests.get(base_url+query+search_filter)
    soup = BeautifulSoup(response.text, 'html.parser')

    number_of_cars = int(soup.find(class_='fleft tab selected').text[8:-2])
    print(f'number_of_cars = {number_of_cars}')

    cars = list()
    for page in range(ceil(number_of_cars/32)):
        if page == 0:
            pass
        else:
            page = f'&page={page+1}'
            response = requests.get(base_url + query + search_filter + page)
            soup = BeautifulSoup(response.text, 'html.parser')

        cars_html = soup.find_all(class_='offer-item__content ds-details-container')

        for car in cars_html:
            title = car.find(class_='offer-item__title').h2.a['title']
            month = car.find(class_='ds-params-block').find(attrs={'data-code': 'first_registration_month'}).span.text
            year = car.find(class_='ds-params-block').find(attrs={'data-code': 'first_registration_year'}).span.text
            mileage = car.find(class_='ds-params-block').find(attrs={'data-code': 'mileage'}).span.text
            power = car.find(class_='ds-params-block').find(attrs={'data-code': 'power'}).span.text

            price = car.find(class_='offer-item__price').div.span.span.text

            date = ' '.join([months[month], year])
            title = f'{title} ({power})'

            cars.append([title, date, mileage[:-3].replace(' ', ''), price.replace(' ', '')])

    return cars


auris = 'toyota/auris/desde-2011/'
fabia = 'skoda/fabia/desde-2015/'
rio = 'kia/rio/desde-2011/'
mazda2 = 'mazda/2/desde-2014/'
jazz = 'honda/jazz/desde-2013/'
i20 = 'hyundai/i20/desde-2014/'
micra = 'nissan/micra/desde-2017/'
yaris = 'toyota/yaris/desde-2012/'
scala = 'skoda/scala/'
ceed = 'kia/ceed/'
focus = 'ford/focus/desde-2017/'


cars = search(focus)

cars.sort(key=lambda k: int(k[2]))
for car in cars:
    print('\t'.join(car))
