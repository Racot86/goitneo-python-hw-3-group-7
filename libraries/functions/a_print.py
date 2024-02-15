import time, random
from libraries.classes.class_colors import colors


def a_print(data, prefix='', wait_after=0.1, main_color='', prefix_color='',speed=0.01):
    n = 1
    s = ''
    for line in data:
        s += line
        if s != data:
            print(prefix_color + prefix + colors.CEND + main_color + s + colors.CEND, end='\r')
            time.sleep(speed)
        else:
            print(prefix_color + prefix + colors.CEND + main_color + s + colors.CEND, end='')
            print(end='\n')
            time.sleep(wait_after)
        n += 1


if __name__ == '__main__':
    a_print('Hello', prefix='say: ')
