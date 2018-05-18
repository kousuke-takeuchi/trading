import os
import zipfile

import requests
from bs4 import BeautifulSoup

import numpy as np
import pandas as pd

from pairs import PAIR_LIST

DOMAIN = 'http://www.histdata.com'
BASE_URL = DOMAIN + '/download-free-forex-data/?/ascii/1-minute-bar-quotes/{}'


def download(url, form, path=None, ignore_exists=True):
    if path is None:
        path = '.data/{}/{}.zip'.format(form['fxpair'], form['datemonth'])
    extract_path = path.split('.zip')[0]
    print(extract_path)

    if ignore_exists and os.path.exists(path):
        return

    # フォルダ作成
    dir_path = '/'.join(path.split('/')[:-1])
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    url = DOMAIN + '/get.php'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,ja;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'complianceCookie=on; OAS_SC1=1526630173192',
        'Host': 'www.histdata.com',
        'Origin': 'http://www.histdata.com',
        'Pragma': 'no-cache',
        'Referer': url,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    }
    res = requests.post(url, data=form, headers=headers, stream=True)
    if res.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
        with zipfile.ZipFile(path) as zf:
            zf.extractall(path=extract_path)


def get_pair_monthly_link(pair):
    res = requests.get(BASE_URL.format(pair))
    soup = BeautifulSoup(res.content, 'html.parser')
    link_tags = soup.select('.page-content p > a')
    urls = [DOMAIN + tag['href'] for tag in link_tags]
    return urls

def get_download_form(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    hiddens = soup.select('form#file_down input[type="hidden"]')
    return dict([[hidden["name"], hidden["value"]] for hidden in hiddens])


def download_local(path='.data', pair=None, ignore_exists=True):
    # 全てのペアリストに対してダウンロード先のリンクを取得
    pair_list = [pair] if pair else PAIR_LIST
    for pair in PAIR_LIST:
        urls = get_pair_monthly_link(pair)
        for url in urls:
            form = get_download_form(url)
            download(url, form, ignore_exists=ignore_exists)

# dfのデータからtfで指定するタイムフレームの4本足データを作成する関数
def TF_ohlc(df, tf):
    x = df.resample(tf).ohlc()
    O = x['Open']['open']
    H = x['High']['high']
    L = x['Low']['low']
    C = x['Close']['close']
    ret = pd.DataFrame({'Open': O, 'High': H, 'Low': L, 'Close': C},
                       columns=['Open','High','Low','Close'])
    return ret.dropna()


def load_local(pair, year, tf='H', path='.data'):
    """
    【参考】 https://qiita.com/toyolab/items/e8292d2f051a88517cb2
    [tf]
    分 - 'T'
    時 - 'H'
    日 - 'D'
    週 - 'W'
    月 - 'M'
    """
    filename = os.path.join(path, pair, year, 'DAT_ASCII_{}_M1_{}.csv'.format(pair, year))
    dataM1 = pd.read_csv(filename, sep=';',
                         names=('Time','Open','High','Low','Close', ''),
                         index_col='Time', parse_dates=True)
    dataM1.index += pd.offsets.Hour(7) #7時間のオフセット
    ohlc = TF_ohlc(dataM1, tf)
    return ohlc


if __name__ == '__main__':
    # データのダウンロード
    # download_local()

    # 一週間ごとのデータを取得
    data = load_local('EURUSD', '2017', tf='W')
    print(data)
