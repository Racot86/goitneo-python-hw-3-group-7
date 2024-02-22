from libraries.classes.class_address_book import AddressBook, Record
from libraries.classes.class_colors import colors

from libraries.functions.a_print import a_print


c_title = colors.CGREEN
c_end = colors.CEND
c_cmd = colors.CGREEN2
c_bold = colors.CBOLD
c_cmd_text = colors.CYELLOW2
c_warning = colors.CRED


def error_test(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as err:
            a_print(err, prefix='WARNING: ', prefix_color=c_warning, main_color=c_title)
        except IndexError:
            a_print('wrong number of arguments', prefix='WARNING: ', prefix_color=c_warning, main_color=c_title)

    return inner


def extract_value(what, from_to):
    return from_to.replace(what, '')


def parameter_getter(cmd):
    contact = Record(cmd[0])
    for i in range(1, len(cmd)):
        par = cmd[i]
        par = par.strip()

        psn = par.find('bday:')
        if psn != -1:
            contact.add_birth_day(extract_value('bday:', par))
            continue

        psn = par.find('tel:')
        if psn != -1:
            val = extract_value('tel:', par)
            contact.add_phone(val.split(','))
            continue

        psn = par.find('address:')
        if psn != -1:
            contact.add_address(extract_value('address:', par))
            continue

        psn = par.find('fav:')
        if psn != -1:
            contact.add_favorite(extract_value('fav:', par))
            continue

        psn = par.find('note:')
        if psn != -1:
            contact.add_note(extract_value('note:', par))
            continue

        psn = par.find('email:')
        if psn != -1:
            contact.add_email(extract_value('email:', par))
            continue

    return contact


@error_test
def add_command(cmd, contacts):
    cmd.pop(0)
    if len(cmd) > 0:
        contacts = AddressBook(contacts)
        contact = parameter_getter(cmd)
        contacts.add_record(contact)
    else:
        a_print('Wrong parameters', main_color=c_title, prefix='  WARNING! ', prefix_color=c_warning)
    return contacts
