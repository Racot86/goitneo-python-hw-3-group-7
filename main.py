# importing py files
from libraries.classes.class_address_book import Record, AddressBook
from libraries.classes.class_colors import colors

from libraries.functions.boiler_plate import boiler_plate
from libraries.functions.a_print import a_print
from libraries.functions.cls_command import cls
from libraries.functions.format_command import format_command
from libraries.functions.add_command import add_command
from libraries.functions.hello_command import hello_command
from libraries.functions.load_contacts import load_contacts
from libraries.functions.save_contacts import save_contacts
from libraries.functions.show_command import show_command
from libraries.functions.delete_command import delete_command
from libraries.functions.change_command import change_command

# defining contacts  user list
contacts = AddressBook(load_contacts())

# defining theme colors
c_title = colors.CGREEN
c_end = colors.CEND
c_cmd = colors.CGREEN2
c_bold = colors.CBOLD
c_cmd_text = colors.CYELLOW2
c_warning = colors.CRED


# main function for command implementation
def process_command(cmd):
    global contacts
    match cmd[0]:
        case "add":
            add_command(cmd, contacts)
            contacts = load_contacts()
            # print(contacts)
        case "hello":
            hello_command()
        case "clear":
            cls()
        case "show":
            show_command(cmd, contacts)
        case "delete":
            contacts = delete_command(cmd, contacts)
        case "change":
            contacts = change_command(cmd, contacts)
            contacts = load_contacts()
        case _:
            a_print('Command not recognized',
                    wait_after=0.5,
                    main_color=c_title,
                    prefix='  WARNING: ',
                    prefix_color=c_warning + c_bold
                    )


# starting test of app
boiler_plate()

a_print(' .................. ' + c_bold + c_cmd + str(len(contacts)) + c_end + c_title + ' contacts',
        main_color=c_bold + c_title,
        prefix='ADDRESS BOOK',
        prefix_color=c_cmd)
print('')
a_print('Welcome to P.E.R.S.S.Y.! ' + c_cmd + 'Enter help command' + c_end + c_title + ' to view available options',
        prefix='MESSAGE: ',
        prefix_color=c_cmd + c_bold,
        main_color=c_title)


# main loop of app
def main():
    while True:
        cmd = input('\n' + c_cmd + c_bold + 'COMMAND> ' + c_end + c_cmd)
        a_print('processing <' + c_cmd + c_bold + cmd + c_end + c_title + '> command . . .', prefix='> ',
                prefix_color=c_bold + c_cmd, main_color=c_title)
        print('')
        if format_command(cmd)[0] in ['exit', 'end', 'quit']:
            break
        else:
            process_command(format_command(cmd))


if __name__ == '__main__':
    main()
