from libraries.classes.class_colors import colors

from libraries.functions.a_print import a_print

c_title = colors.CGREEN
c_end = colors.CEND


def boiler_plate():
    a_print('--------------------------------------------------', main_color=c_title)
    print(c_title + ' P.E.R.S.S.Y. - Personal Assistant Terminal v 1.2')
    a_print('--------------------------------------------------', main_color=c_title)