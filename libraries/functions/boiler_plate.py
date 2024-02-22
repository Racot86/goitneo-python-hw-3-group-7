from libraries.classes.class_colors import colors
import time
import random
import math


from libraries.functions.a_print import a_print

c_title = colors.CGREEN
c_end = colors.CEND
c_cmd = colors.CGREEN2
c_bold = colors.CBOLD


def boiler_plate():
    sl = 0.2
    for i in range(3):
        print(c_title + '-------------------------------------------------', end='\r')
        time.sleep(sl)
        print(c_cmd + '-------------------------------------------------', end='\r')
        sl -= 0.05
        time.sleep(sl)
    print(c_cmd + '-------------------------------------------------' + c_end)

    text = c_title + ' P.E.R.S.S.Y. - Personal Assistant Terminal v1.3' + c_end
    l_text = list(text)
    for i in range(6, len(l_text) - 5):

        l_text = list(text)
        l_text[i - 1] = c_cmd + l_text[i - 1] + c_end + c_title
        l_text[i] = c_cmd + c_bold + l_text[i] + c_end + c_title
        l_text[i + 1] = c_cmd + l_text[i + 1] + c_end + c_title
        p = ''.join(l_text)
        print(p, end='\r')
        time.sleep(0.03)
    print(f' {c_cmd}P.E.R.S.S.Y.{c_end + c_title} - Personal Assistant Terminal v1.3')
    print(c_cmd + '-------------------------------------------------' + c_end)

