from kbsp_schedule import getting, parsing
from os import path

cources = {'1 курс': ['F2', 'K2', 'P2']}

schedule_dir = path.join('.', 'schedule')
getting.get_schedule(schedule_dir)

parsing.pars_main(schedule_dir, 'F2', 'K2', 'P2', 'Z2', 'AE2', 'AJ2', 'AT2', 'AY2', 'BD2')