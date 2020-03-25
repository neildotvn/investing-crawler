from urllib.request import urlopen, Request
import bs4 as bs
from general import *
import json, datetime, threading

labels_arr = ['silver', 'copper', 'platinum', 'palladium',
              'crude oil wti', 'brent oil', 'natural gas',
              'heating oil', 'london gas oil', 'us corn',
              'us soybeans', "us soybean oil"]
labels_set = set()
for label in labels_arr:
    labels_set.add(label)
INVESTING_URL = 'https://www.investing.com/commodities/real-time-futures'


def crawl_from_investing(url, labels):
    prices = {}
    headers = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'}
    req = Request(url=url, headers=headers)
    try:
        html = urlopen(req)
        soup = bs.BeautifulSoup(html, 'html.parser')
        table = soup.find('div', id='cross_rates_container')
        rows = table.find_all('tr')

        for row in rows:
            cells = row.find_all('td')
            if len(cells) > 0:
                exchange = cells[0].find_all('span')[0].get('title').lower()
                # print(exchange)
                if exchange.rstrip() == 'united states':
                    exchange = 'nyb'
                elif exchange.rstrip() == 'united kingdom':
                    exchange = 'ice'
                else:
                    continue
                key = cells[1].find_all('a')[0].text.lower()
                if key in labels and key not in prices:
                    temp_arr = []
                    temp = [parse_date_from_investing(cells[2].text.rstrip())]
                    for i in range(4):
                        temp.append(parse_number(cells[i + 3].text.rstrip()))
                    temp.append(0)
                    temp.append(0)
                    if '-' in cells[6].text:
                        temp.append(False)
                    else:
                        temp.append(True)
                    temp[3], temp[4] = temp[4], temp[3]
                    temp[2], temp[3] = temp[3], temp[2]
                    temp_arr.append(temp)

                    prices[key.replace(' ', '_')] = {exchange: temp_arr}

        print('At ' + str(datetime.datetime.now()) + ' successfully crawled from ' + INVESTING_URL)
        return prices
    except Exception as exception:
        print(exception)


def write_json(file_name, prices):
    file = file_name
    write_file(file, json.dumps(prices))


def start():
    write_json('investing.json', crawl_from_investing(INVESTING_URL, labels_set))
    threading.Timer(3, start).start()


start()
