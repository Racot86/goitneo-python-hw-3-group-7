from libraries.classes.class_colors import colors
from libraries.classes.class_address_book import AddressBook
from libraries.functions.save_contacts import save_contacts

from libraries.functions.a_print import a_print

# defining theme colors
c_title = colors.CGREEN
c_end = colors.CEND
c_cmd = colors.CGREEN2
c_bold = colors.CBOLD
c_cmd_text = colors.CYELLOW2
c_warning = colors.CRED


def delete_command(cmd, contacts):
    match = []
    if len(cmd) > 1:
        cmd.pop(0)
        contacts = AddressBook(contacts)
        for contact in cmd:
            for k, check_contact in contacts.items():
                if check_contact.name == contact:
                    match.append(contact)
        if len(match) > 0:
            for c in match:
                contacts.pop(c)
            a_print(c_cmd + ', '.join(match) + ' deleted' + c_end + c_title + ' from the contact list', prefix='< ', prefix_color=c_cmd, main_color=c_title)
            save_contacts(contacts)
        else:
            a_print(c_cmd + ', '.join(cmd) + c_end + c_title + ' contact/s not found', prefix='  WARNING! ', prefix_color=c_cmd_text,
                    main_color=c_title)
        return contacts
    else:
        a_print('Wrong parameters', main_color=c_title, prefix='  WARNING! ', prefix_color=c_warning)
        return contacts
