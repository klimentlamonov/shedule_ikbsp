#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
#
# # # # # # # # # # # # # # # # # # # # # # # # #
# Source: https://github.com/vjki/kbsp_schedule #
# # # # # # # # # # # # # # # # # # # # # # # # #
#
#
import re
import requests
import csv
import time
from openpyxl import load_workbook
from bs4 import BeautifulSoup
from os import path, listdir, remove
from datetime import datetime

# --- Globals ---
url = 'https://www.mirea.ru/schedule/'
ERRORS = {
    'check_schedule': [],
    'get_schedule': []
}


# --- Function ---
def check_schedule(schedule_dir):
    """Write in lmod.csv.
    Check last modified and last update of all files and write it into lmod.csv.
        view(lmod.csv): (course),(file name),(last modified),(last update)

    • schedule_dir - string which contain way to schedule dir

    """
    try:
        remove(path.join(schedule_dir, 'lmod.csv'))
        for sub_dir in range(1, 6):
            current_dir = path.join(schedule_dir, str(sub_dir))
            for file_name in listdir(current_dir):
                print(f"Working with file \"{file_name}\"...")
                wb = load_workbook(path.join(current_dir, file_name))
                last_modified = wb.properties.modified
                print(f'Last modified {last_modified}')
                with open(path.join(schedule_dir, 'lmod.csv'), 'a', encoding='utf-8') as f:
                    file_writer = csv.writer(f, lineterminator='\n')
                    t = path.getmtime(path.join(current_dir, file_name))
                    last_update = datetime.fromtimestamp(t)
                    file_writer.writerow([sub_dir, file_name, last_modified, last_update])
                    print('Write SUCCESS', end='\n\n')
    except OSError as e:
        print(f'ERROR. {e}', end='\n\n')
        ERRORS['check_schedule'].append(f'ERROR. {e}')


def get_schedule(schedule_dir):
    """Downloading schedules.
    Download kbsp schedules from site mirea and put them into
    directories.
        View: schedule -> 1(number of semester)

    • schedule_dir - string which contain way to schedule dir

    """
    r = requests.get(url)
    soup = BeautifulSoup(r.text, features="html.parser")
    links = soup.find_all(href=re.compile(r"КБиСП.*xlsx"))
    for link in links:
        file_name = link.get('href').split('/')[-1]
        print('Downloading ' + file_name + '... ')
        with open(path.join(schedule_dir, file_name.split()[1], file_name), 'wb') as f:
            urf = requests.get(link.get('href'))
            f.write(urf.content)
        print('SUCCESS', end="\n\n")


if __name__ == "__main__":
    get_schedule(path.join('..', 'schedule'))
    check_schedule(path.join('..', 'schedule'))
