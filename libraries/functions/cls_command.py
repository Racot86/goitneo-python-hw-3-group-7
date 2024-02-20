from os import system, name
from libraries.functions.boiler_plate import boiler_plate


def cls():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    boiler_plate()


