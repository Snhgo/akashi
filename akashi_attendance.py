# coding:utf-8
import requests
from bs4 import BeautifulSoup

# セッションを開始
session = requests.session()

def login(session, user, password):

    url_login = "https://atnd.ak4.jp/login"
    res = session.get(url_login)
    soup = BeautifulSoup(res.text, 'html.parser')
    authTag = soup.select_one('input[name="authenticity_token"]')
    # ログイン
    login_info = {
        'form[company_id]': '',
        'form[login_id]': user,
        'form[password]': password,
        'authenticity_token': authTag.attrs['value']
    }

    # action
    res = session.post(url_login, data=login_info)
    return res;

user=''
password=''
res = login(session, user, password)

print(res.text)
