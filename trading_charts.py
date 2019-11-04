from urllib.request import urlopen, Request
import bs4 as bs
from general import *
import json
import datetime


dict_products_urls = {
    'corn': 'https://data.tradingcharts.com/futures/quotes/ZC.html',
    'soybean_oil': 'https://data.tradingcharts.com/futures/quotes/ZL.html',
    'soybeans': 'https://data.tradingcharts.com/futures/quotes/ZS.html',
    'copper': 'https://data.tradingcharts.com/futures/quotes/HG.html',
    'silver': 'https://data.tradingcharts.com/futures/quotes/SI.html',
    'sugar': 'https://data.tradingcharts.com/futures/quotes/SB.html',
    'brent_crude_oil': 'https://data.tradingcharts.com/futures/quotes/QA.html',
    'natural_gas': 'https://data.tradingcharts.com/futures/quotes/NG.html',
    'platinum': 'https://data.tradingcharts.com/futures/quotes/PL.html',
}


def crawl_from_trading_charts(url):
    prices = {}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url=url, headers=headers)
    try:
        html = urlopen(req)
        soup = bs.BeautifulSoup(html, 'html.parser')
        table = soup.find('table', id='tblQuote')
        rows = table.find_all('tr')

        for row in rows:
            print(row)
        #     cells = row.find_all('td')
        #     if len(cells) > 0:
        #         exchange = cells[0].find_all('span')[0].get('title').lower()
        #         # print(exchange)
        #         if exchange.rstrip() == 'united states':
        #             exchange = 'nyb'
        #         elif exchange.rstrip() == 'united kingdom':
        #             exchange = 'ice'
        #         else:
        #             continue
        #         key = cells[1].find_all('a')[0].text.lower()
        #         if key in labels and key not in prices:
        #             temp_arr = []
        #             temp = [parse_date_from_investing(cells[2].text.rstrip())]
        #             for i in range(4):
        #                 temp.append(parse_number(cells[i + 3].text.rstrip()))
        #             temp.append(0)
        #             temp.append(0)
        #             if '+' in cells[6].text:
        #                 temp.append(True)
        #             if '-' in cells[6].text:
        #                 temp.append(False)
        #             temp[2], temp[4] = temp[4], temp[2]
        #             temp_arr.append(temp)
        #
        #             prices[key] = {exchange: temp_arr}
        #
        # print('At ' + str(datetime.datetime.now()) + ' successfully crawled from ' + URL)
        # return prices
    except Exception as exception:
        print(exception)


crawl_from_trading_charts(dict_products_urls['corn'])