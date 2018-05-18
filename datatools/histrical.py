import os
import zipfile

import requests
from bs4 import BeautifulSoup

from pairs import PAIR_LIST

DOMAIN = 'http://www.histdata.com'
BASE_URL = DOMAIN + '/download-free-forex-data/?/metatrader/1-minute-bar-quotes/{}'


def download(url, form, path=None):
    if path is None:
        path = '.data/{}/{}.zip'.format(form['fxpair'], form['datemonth'])
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
    extract_path = path.split('.zip')[0]
    print(extract_path)
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
    soup = BeautifulSoup(res.content)
    hiddens = soup.select('form#file_down input[type="hidden"]')
    return dict([[hidden["name"], hidden["value"]] for hidden in hiddens])

def download_local(path='.data', pair=None):
    # 全てのペアリストに対してダウンロード先のリンクを取得
    pair_list = [pair] if pair else PAIR_LIST
    for pair in PAIR_LIST:
        urls = get_pair_monthly_link(pair)
        for url in urls:
            form = get_download_form(url)
            download(url, form)


def load_local(path='.data'):
    pass


download_local()
# download('EURUSD', '201805', 'cc5f41f1a10f4efc64f3e5c038f127ad')
