import requests
from bs4 import BeautifulSoup

URL_schedule = 'https://aues.arhit.kz/rasp/scheduleNew.php?sg=1594&schedule=22'

HEADERS = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}


def get_html(url, params=None):
    response = requests.get(url, headers=HEADERS, params=params)
    return response

def get_rasp(html):
    soup = BeautifulSoup(html, 'html.parser')
    subject = soup.find('table', class_='table text-light').get_text(strip=True)
    return subject

def parse_schedule():
        global schedule
        html_rasp = get_html(URL_schedule)
        if get_html(URL_schedule).ok:
            schedule = get_rasp(html_rasp.text)
        else:
            print('error')
        return schedule
parse_schedule()
   