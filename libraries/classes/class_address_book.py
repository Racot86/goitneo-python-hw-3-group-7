from collections import UserDict
from libraries.functions.a_print import a_print
from datetime import datetime
from libraries.functions.display_contact_details import display_contact_details
from libraries.functions.save_contacts import save_contacts
from libraries.functions.str_to_bool import str2bool

from libraries.classes.class_colors import colors

c_title = colors.CGREEN
c_end = colors.CEND
c_cmd = colors.CGREEN2
c_bold = colors.CBOLD
c_cmd_text = colors.CYELLOW2
c_warning = colors.CRED


def find_matches(look_up, data):
    match = 0
    for ch in data:
        if ch == look_up:
            match += 1
    return match


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


def date_error_test(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError or TypeError or ValueError:
            a_print('Wrong date format. Format must be dd/mm/yyyy. Birth date will be not added to contact data\n',
                    prefix='WARNING: ',
                    prefix_color=c_warning,
                    main_color=c_title)



    return inner


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.address = ''
        self.birth_date = ''
        self.favorite = False
        self.note = ''
        self.email = ''

    def add_phone(self, phone=[]):
        for p in range(0, len(phone)):
            phone[p] = phone[p].strip()
            try:
                check = int(phone[p])
            except ValueError:
                a_print(f'Phone number <{phone[p]}> must contain {c_cmd}only digits.', prefix='  WARNING! ',
                        main_color=c_title,
                        prefix_color=c_warning)
                a_print(f'Phone number {c_cmd}not added{c_end + c_title} to contact data.', prefix='           ',
                        main_color=c_title,
                        prefix_color=c_warning)
            else:
                if len(phone[p]) == 10:
                    self.phones.append(phone[p])
                else:
                    a_print(f'Phone number <{phone[p]}> must be a {c_cmd}ten{c_end + c_title} digits.',
                            prefix='  WARNING! ',
                            main_color=c_title,
                            prefix_color=c_cmd_text)
                    a_print('Phone number not added to contact data.', prefix='           ',
                            main_color=c_title,
                            prefix_color=c_warning)

    @date_error_test
    def add_birth_day(self, bday=''):
        s_val = bday.split('/')
        try:
            self.birth_date = datetime(int(s_val[2]), int(s_val[1]), int(s_val[0]))
        except ValueError:
            a_print('Wrong date format. Format must be dd/mm/yyyy. Birth date will be not added to contact data\n',
                    prefix='  WARNING: ',
                    prefix_color=c_warning,
                    main_color=c_title)


    def add_email(self, email):
        if find_matches('@', email) == 1 and find_matches('.', email) != 0:
            self.email = email
        else:
            a_print('Wrong e-mail format. e-mail will not be added to contact data', prefix=' WARNING! ',
                    prefix_color=c_warning,
                    main_color=c_title)

    def add_address(self, address):
        self.address = address.strip()

    def add_note(self, note):
        self.note = note.strip().replace('_', ' ')

    def add_favorite(self,fav):
        self.favorite = str2bool(fav)



class AddressBook(UserDict):
    def add_record(self, record):
        if record.name not in self.data:
            self.data[record.name] = record
            a_print('contact ' + c_bold + c_cmd + f'{record.name} ' + c_end + c_title + 'added to contacts',
                    prefix='< ',
                    main_color=c_title,
                    prefix_color=c_bold + c_cmd)
            display_contact_details(record)
            save_contacts(self.data)
        else:
            a_print(f'Contact with name {c_cmd}<{record.name}> {c_title}already exists.', prefix='  WARNING! ',
                    prefix_color=c_cmd_text,
                    main_color=c_title)
            while True:
                answer = input('< Would you like to change contact name?(Y/N)> ')
                if answer.lower() in ['y', 'yes']:
                    answer = input('< Insert contact name> ')
                    if answer != '':
                        if answer not in self.data:
                            record.name = answer
                            self.data[record.name] = record
                            a_print(
                                'contact ' + c_bold + c_cmd + f'{record.name} ' + c_end + c_title + 'added to contacts',
                                prefix='< ',
                                main_color=c_title,
                                prefix_color=c_bold + c_cmd)
                            display_contact_details(record)
                            save_contacts(self.data)
                            break
                        else:
                            a_print(f'Contact with name {c_cmd}<{answer}> {c_title}already exists.',
                                    prefix='  WARNING! ',
                                    prefix_color=c_cmd_text,
                                    main_color=c_title)
                else:
                    a_print(f'Operation {c_cmd}aborted.', prefix='< ', prefix_color=c_cmd, main_color=c_title)
                    break

    def records(self):
        return self.data
