#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
#
# # # # # # # # # # # # # # # # # # # # # # # # #
# Source: https://github.com/vjki/kbsp_schedule #
# # # # # # # # # # # # # # # # # # # # # # # # #
#
#
import csv
from kbsp_schedule import getting, parsing
from os import path
from datetime import datetime


def check_lmod():
    with open(path.join('.', 'schedule', 'lmod.csv'), 'r', encoding='utf-8') as rf:
        reader = csv.reader(rf)
        for row in reader:
            print(row[1])
            print(f"Last update of the file {row[-1]}")
            print(f"Last modified of the file {row[-2]}", end="\n\n")


if __name__ == "__main__":
    print("This service checks and downloads the schedule of mirea kbsp.")
    check_lmod()
    ans = input("Wana update? ['y' for Yes, 'n' for No]")
    if ans == 'y':
        getting.get_schedule(path.join('.', 'schedule'))
        getting.check_schedule(path.join('.', 'schedule'))
        print("Done.")
        check_lmod()
