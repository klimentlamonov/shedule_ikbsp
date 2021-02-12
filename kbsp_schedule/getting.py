import requests
from bs4 import BeautifulSoup
import re
from os import path

# --- Globals ---
url = 'https://www.mirea.ru/schedule/'


# --- Function ---
def get_schedule(schedule_dir):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")

    links = soup.find_all(href=re.compile(r"КБиСП.*xlsx"))
    for link in links:
        print('Downloading ' + link.get('href').split('/')[-1] + '... ')
        with open(path.join(schedule_dir, link.get('href').split('/')[-1]), 'wb') as f:
            urf = requests.get(link.get('href'))
            f.write(urf.content)
        print('SUCCESS', end="\n\n")


if __name__ == "__main__":
    get_schedule(path.join('..', 'schedule'))
