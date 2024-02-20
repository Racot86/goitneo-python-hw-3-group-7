from libraries.classes.class_colors import colors

from libraries.functions.a_print import a_print

c_title = colors.CGREEN
c_end = colors.CEND
c_cmd = colors.CGREEN2
c_bold = colors.CBOLD
c_cmd_text = colors.CYELLOW2
c_warning = colors.CRED


def replace_empty_string_with_empty(data):
    if data == '':
        return '<no data>'
    else:
        return data


def display_contact_details(contact):
    a_print('CONTACT DETAILS', main_color=c_title, prefix='< ', prefix_color=c_cmd)
    a_print('{:>15}: {:<20}'.format('name', contact.name + ' <' + contact.note + '>'), main_color=c_cmd)

    if contact.birth_date != '':
        a_print(
            '{:>15}: {:<20}'.format('birth date', replace_empty_string_with_empty(contact.birth_date.strftime("%d-%m-%Y"))),
            main_color=c_cmd)
    else:
        a_print('{:>15}: {:<20}'.format('birth date','<no data>'), main_color=c_cmd)
    a_print('{:>15}: {:<20}'.format('tel', replace_empty_string_with_empty(', '.join(contact.phones))),
            main_color=c_cmd)
    a_print('{:>15}: {:<20}'.format('e-mail', replace_empty_string_with_empty(contact.email)), main_color=c_cmd)
    a_print('{:>15}: {:<20}'.format('address', replace_empty_string_with_empty(contact.address)), main_color=c_cmd)
    a_print(
        '{:>15}: {:<20}'.format('in favorites', str(contact.favorite)), main_color=c_cmd)
