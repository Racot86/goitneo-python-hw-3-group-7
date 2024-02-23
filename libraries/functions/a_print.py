import time, random
from libraries.classes.class_colors import colors
import re

c_title = colors.CGREEN
c_end = colors.CEND
c_cmd = colors.CGREEN2
c_bold = colors.CBOLD
c_cmd_text = colors.CYELLOW2
c_warning = colors.CRED


def a_print(data, prefix='', wait_after=0.1, main_color='', prefix_color='', speed=0.01, end='\n'):
    def find_codes(codes, main_string):
        matches = {}
        for code in codes:
            start_index = 0
            for i in range(len(main_string)):
                j = main_string.find(code, start_index)
                if j != -1:
                    matches[j] = code
                    start_index = j + 1
        return matches

    m = find_codes(colors.check_names, data)
    p = 0
    output = ''
    while p <= len(data):

        time.sleep(speed)
        if p in m:
            p += len(m[p])
        else:
            p += 1
        output = prefix_color + prefix + colors.CEND + main_color + data[0: p] + '\u2588' + colors.CEND
        print(output, end='\r')
    print(output.replace('\u2588', ' '))


if __name__ == '__main__':
    a_print('Hello', prefix='say: ')
