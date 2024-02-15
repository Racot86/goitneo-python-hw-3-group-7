from libraries.classes.class_address_book import Record, AddressBook, Phone
from libraries.classes.class_colors import colors

from libraries.functions.boiler_plate import boiler_plate
from libraries.functions.a_print import a_print
from libraries.functions.cls_command import cls
from libraries.functions.format_command import format_command
from libraries.functions.add_command import add_command

contacts = AddressBook()

c_title = colors.CGREEN
c_end = colors.CEND
c_cmd = colors.CGREEN2
c_bold = colors.CBOLD
c_cmd_text = colors.CYELLOW2
c_warning = colors.CRED


def process_command(cmd):
    match cmd[0]:
        case "add":
            add_command(cmd)
        case _:
            a_print('Command not recognized',
                    wait_after=0.5,
                    main_color=c_title,
                    prefix='  WARNING: ',
                    prefix_color=c_warning + c_bold
                    )


boiler_plate()
a_print('Welcome to P.E.R.S.S.Y.!',
        prefix='MESSAGE: ',
        prefix_color=c_cmd_text,
        main_color=c_title)
a_print('enter help command to view available options',
        prefix='         ',
        main_color=c_title)


def main():
    while True:
        cmd = input('\n' + c_cmd + c_bold + 'COMMAND> ' + c_end)
        a_print('-------------------------------------', speed=0.009, main_color=c_title, prefix='  ')
        #cls()
        #boiler_plate()
        a_print(cmd, prefix='> ', prefix_color=c_bold + c_cmd, main_color=c_bold + c_cmd)
        if format_command(cmd)[0] in ['exit', 'end', 'quit']:
            break
        else:
            process_command(format_command(cmd))


if __name__ == '__main__':
    main()
