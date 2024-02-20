from libraries.classes.class_address_book import AddressBook, Record
from libraries.classes.class_colors import colors

from libraries.functions.a_print import a_print
from libraries.functions.display_contact_details import display_contact_details
from libraries.functions.str_to_bool import str2bool

from datetime import datetime
from libraries.functions.save_contacts import save_contacts

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
            if func.__name__ == 'convert_string_to_date':
                a_print('Wrong date format. Birth date will not be changed\n', prefix='WARNING: ',
                        prefix_color=c_warning, main_color=c_title)
                return ''
            else:
                a_print('wrong number of arguments', prefix='WARNING: ', prefix_color=c_warning, main_color=c_title)
        except TypeError as err:
            if func.__name__ == 'add_command':
                a_print('Contact has error in telephone number.', prefix='  WARNING! ',
                        prefix_color=c_warning,
                        main_color=c_title)

    return inner


def contact_not_exists(contact, contacts):
    match = False
    for c in contacts:
        if c == contact:
            match = True
            break
    if not match:
        return True
    else:
        return False


@error_test
def convert_string_to_date(val):
    s_val = val.split('/')
    return datetime(int(s_val[2]), int(s_val[1]), int(s_val[0]))


@error_test
def check_phone_format(val):
    for p in val:
        if len(p) <= 10:
            if not p.isdigit():
                val.remove(p)
                a_print('Contact has wrong phone number/s', prefix='WARNING: ', prefix_color=c_warning,
                        main_color=c_title)
        else:
            a_print('Wrong number length. Number cannot be longer than 10 digits. Number will not be added to '
                    'contact', prefix='WARNING: ', prefix_color=c_warning, main_color=c_title)
            val.remove(p)
    return val


def extract_value(what, from_to):
    return from_to.replace(what, '')


def parameter_getter(cmd, contact, contacts):
    for i in range(1, len(cmd)):
        par = cmd[i]
        par = par.strip()

        psn = par.find('bday:')
        if psn != -1:
            val = extract_value('bday:', par)
            check = convert_string_to_date(val)
            if check != '':
                contact.birth_date = check
            continue

        psn = par.find('tel:')
        if psn != -1:
            val = extract_value('tel:', par)
            contact.phones = check_phone_format(val.split(','))
            continue

        psn = par.find('address:')
        if psn != -1:
            val = extract_value('address:', par)
            contact.address = val
            continue

        psn = par.find('fav:')
        if psn != -1:
            val = extract_value('fav:', par)
            contact.favorite = str2bool(val)
            continue

        psn = par.find('note:')
        if psn != -1:
            val = extract_value('note:', par)
            contact.note = val.replace('_', ' ')
            continue

        psn = par.find('email:')
        if psn != -1:
            val = extract_value('email:', par)
            contact.email = val
            continue

        psn = par.find('name:')
        if psn != -1:
            val = extract_value('name:', par)
            if contact_not_exists(val, contacts):
                contacts[val] = contact
                contacts.pop(contact.name)
                contact.name = val
            else:
                a_print(f'contact with name {val} already exists')
            continue

    return contacts


def change_command(cmd, contacts):
    if len(cmd) > 1:
        cmd.pop(0)
        match = False
        for k, contact in contacts.items():
            if cmd[0] == k:
                edited_contacts = parameter_getter(cmd, contact, contacts)
                a_print('contact data of' + c_cmd + f' <{contact.name}>' + c_end + c_title + ' updated', prefix='< ',
                        prefix_color=c_cmd,
                        main_color=c_title)
                match = True
                display_contact_details(contact)
                save_contacts(edited_contacts)
                return edited_contacts
        if not match:
            a_print('Contact not found', prefix=" WARNING! ", main_color=c_title, prefix_color=c_cmd_text)
            return contacts

