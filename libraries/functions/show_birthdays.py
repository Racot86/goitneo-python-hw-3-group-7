from libraries.classes.class_colors import colors

from libraries.functions.a_print import a_print
from datetime import datetime, timedelta

c_title = colors.CGREEN
c_end = colors.CEND
c_cmd = colors.CGREEN2
c_bold = colors.CBOLD
c_cmd_text = colors.CYELLOW2
c_warning = colors.CRED


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def output_month(data):
    if len(data) > 0:
        match_dict = {}
        for c in data:
            i = c['contact']
            match_dict[i['name']] = datetime(datetime.now().year, i['birthday'].month, i['birthday'].day)
        print('\n' + spaces + perssy + 'This month birthdays:\n')

        new_d = dict(sorted(match_dict.items(), key=lambda item: item[1]))

        for k, v in new_d.items():
            print('               ' + "{:>20}: {:<15}".format(c_highlight + v.strftime("%d/%m") + c_end, k))
        print('\n')

    else:
        print('               ' + c_wrong + '<no birthdays>' + c_end)


def output_week(data):
    wk_list = {'Monday': [],
               'Tuesday': [],
               'Wednesday': [],
               'Thursday': [],
               'Friday': [],
               'Saturday': [],
               'Sunday': []
               }
    for c in data:
        i = c['contact']
        wk = c['weekday']
        wk_list[weekdays[wk]].append(i.name)
    for wk, names in wk_list.items():
        if (len(names)) > 0:
            a_print("{:>12}: {:<15}".format(wk, ', '.join(names)), main_color=c_cmd)
        else:
            a_print("{:>12}: {:<15}".format(wk, '<no birthdays>'),main_color=c_title)
    print('\n')


def match_time(today, time_range, contacts):
    array = []
    for c in contacts.values():
        if c.birth_date != '':
            check1 = datetime(today.year, c.birth_date.month, c.birth_date.day)
            d1 = (check1.date() - today.date()).days
            if 0 <= d1 <= time_range:
                array.append({'contact': c, 'weekday': check1.weekday()})

            check2 = datetime(today.year + 1, c.birth_date.month, c.birth_date.day)
            d2 = (check2.date() - today.date()).days
            if 0 <= d2 <= time_range:
                array.append({'contact': c, 'weekday': check2.weekday()})

    return array


def get_time_delta_for_next_week(wk_date):
    wk_day = wk_date.weekday()
    delta = 0
    if wk_day != 0:
        delta = 7 - wk_day
    return delta


def upcoming_birthday(cmd):
    cmd.pop(0)
    if len(cmd) == 2 and cmd[1].lower() == 'birthdays':
        today = datetime.now()
        # today = datetime(2024,12,22)
        match_list = []
        match cmd[0].lower():
            case 'week':
                next_week_monday = today + timedelta(days=get_time_delta_for_next_week(today))
                output_week(match_time(next_week_monday, 6))
            case 'month':
                eom = datetime(today.year, today.month + 1, 1) - timedelta(days=1)
                output_month(match_time(today, (eom.date() - today.date()).days))
            case _:
                print(
                    '\n' + spaces + perssy + c_wrong + 'Time period for command upcoming birthdays not recognised.' + c_end + '\n')

    else:
        print('\n' + spaces + perssy + c_wrong + 'Command not recognised.' + c_end + '\n')


def this_week_birthday(contacts):
    today = datetime.now()
    next_week_monday = today + timedelta(days=get_time_delta_for_next_week(today))
    output_week(match_time(next_week_monday, 6, contacts))
