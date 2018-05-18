import datetime

import requests
from bs4 import BeautifulSoup


class CalendarItem:
    def __init__(self, date, indices):
        self.date = date
        self.indices = indices

    def __str__(self):
        indices_str = ''
        for indice in self.indices:
            indices_str += str(indice) + '\n'
        return '日付: {}\n指標一覧:\n{}'.format(self.date.isoformat(), indices_str)

class Indice:
    def __init__(self, time, name, star, hl):
        self.time = time
        self.name = name
        self.star = star
        self.hl = hl

    def __str__(self):
        objs = [
            ['発表時間', self.time],
            ['指標', self.name],
            ['重要度', self.star],
            ['前回変動幅', self.hl]]
        return '\n'.join(['  {}: {}'.format(obj[0], obj[1]) for obj in objs]) + '\n'


URL = 'https://fx.minkabu.jp/indicators'

def parse_date(date_str):
    # ex. 05/18(金)
    month = int(date_str[0:2])
    day = int(date_str[3:5])
    return datetime.date(2018, month, day)

def match_class(tag, target):
    classes = tag.get('class', [])
    return target in classes

def parse_daily_indices(table):
    rows = table.select('tr')
    indices = []
    for row in rows:
        # '.ei-list-item'があれば新規指標
        if match_class(row, 'ei-list-item'):
            time = row.select('td.time')[0].text
            name = row.select('a.name')[0].text.strip('\n')
            star = len(row.select('td.star')[0].findAll(attrs={'alt': 'Star fill'}))
            hl = row.select('td.hl')[0].text.strip('\n').strip()
            indice = Indice(time=time, name=name, star=star, hl=hl)
            indices.append(indice)
    return indices

def fetch():
    res = requests.get(URL)
    soup = BeautifulSoup(res.content, 'html.parser')
    lists = soup.select('main#main .box .l-section_interval')[1]
    headers = [parse_date(h2.text) for h2 in lists.select('h2')]
    tables = [parse_daily_indices(table) for table in lists.select('table')]

    calendar = []
    for i in range(len(headers)):
        ci = CalendarItem(headers[i], tables[i])
        calendar.append(ci)
    return calendar

__all__ = ['fetch']
