from datetime import datetime

from libraries.functions.a_print import a_print

from libraries.classes.class_colors import colors

c_title = colors.CGREEN
c_end = colors.CEND
c_cmd = colors.CGREEN2
c_bold = colors.CBOLD
c_cmd_text = colors.CYELLOW2
c_warning = colors.CRED


def hello_command():
    time_of_day = ''
    time = datetime.now()
    if 0 <= time.hour < 12: time_of_day = 'morning'
    if 12 <= time.hour < 18: time_of_day = 'day'
    if 18 <= time.hour <= 23: time_of_day = 'evening'
    a_print(c_cmd + f'Good {time_of_day}! ' + c_end + c_title + 'How can I help you?',
            prefix='< ',
            main_color=c_title,
            prefix_color=c_bold + c_cmd)
