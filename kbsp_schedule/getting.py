import re, requests
from openpyxl import load_workbook
from bs4 import BeautifulSoup
from os import path, listdir

# --- Globals ---
url = 'https://www.mirea.ru/schedule/'


# --- Function ---
def check_schedule(schedule_dir):
    for sub_dir in range(1, 6):
        current_dir = path.join(schedule_dir, str(sub_dir))
        for file_name in listdir(current_dir):
            print(f"Checking file {file_name}...")
            wb = load_workbook(path.join(current_dir, file_name))
            print('Last modified %s' % wb.properties.modified, end='\n\n')


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
    # get_schedule(path.join('..', 'schedule'))
    check_schedule(path.join('..', 'schedule'))
