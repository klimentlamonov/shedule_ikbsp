import openpyxl
from os import path


def main():
    # читаем excel-файл
    wb = openpyxl.load_workbook(path.join('.', 'static', 'schedule', '5.xlsx'))

    # получаем активный лист
    sheet = wb.active

    print(sheet['Z2'].value)

    for row in sheet['Z4':'AC75']:
        for cell in row:
            print(cell.coordinate, cell.value)
        print("--END--")


if __name__ == "__main__":
    main()
