import time, random
from libraries.classes.class_colors import colors

c_title = colors.CGREEN
c_end = colors.CEND
c_cmd = colors.CGREEN2
c_bold = colors.CBOLD
c_cmd_text = colors.CYELLOW2
c_warning = colors.CRED


def a_print(data, prefix='', wait_after=0.1, main_color='', prefix_color='',speed=0.01, end='\n'):
    n = 1
    s = ''
    for line in data:
        s += line
        if s != data:
            print(prefix_color + prefix + colors.CEND + main_color + s + '\u2588', end='\r')
            time.sleep(speed)
        else:
            print(prefix_color + prefix + colors.CEND + main_color + s + colors.CEND, end='')
            print(end=end)
            time.sleep(wait_after)
        n += 1


if __name__ == '__main__':
    a_print('Hello', prefix='say: ')
