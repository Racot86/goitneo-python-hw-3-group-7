from libraries.classes.class_colors import colors

# colors to be used in design
c_title = colors.CGREEN
c_end = colors.CEND
c_cmd = colors.CGREEN2
c_bold = colors.CBOLD
c_cmd_text = colors.CYELLOW2
c_warning = colors.CRED

spaces = '     '


def help_command():
    cmd_list = [
        {'cmd': 'show',
         'syntax': 'show <contact name> or <contacts> or <birthdays next week> or <birthdays this month>',
         'short': 'Displays contact details or list of available contacts.',
         'example': 'show Dmytro, show contacts, show Dmytro tel, show birthdays next week, show birthdays next month, show favorites',
         },
        {'cmd': 'add',
         'syntax': 'add <contact name> <tel:data> <bday:dd/mm/yyyy> <fav:(false or true)> <email:data> <note:data>',
         'short': 'Adds contact to contact list.',
         'example': 'add Dmytro, add Dmytro bday:04/06/1986, add Dmytro bday:04/06/1986 tel:0970279618',
         },
        {'cmd': 'delete',
         'syntax': 'delete <contact name> or any number of contacts separated by spaces.',
         'short': 'deletes contact from contact list.',
         'example': 'delete Dmytro, delete Dmytro Olia',
         },
        {'cmd': 'change',
         'syntax': 'change <contact name> <name:data> <tel:data> <bday:dd/mm/yyyy> <fav:(false or true)> <email:data> <note:data>',
         'short': 'Changes contacts data. ',
         'example': 'change Dmytro, change Dmytro bday:09/06/1986, change Dmytro name:Dmytro2 bday:04/06/1986 tel:0970279618',
         },
        {'cmd': 'clear',
         'syntax': 'clear',
         'short': 'clears screen',
         'example': 'clear',
         },
        {'cmd': 'hello',
         'syntax': 'hello',
         'short': 'P.E.R.S.S.Y. will great you',
         'example': 'hello',
         },
        {'cmd': 'exit',
         'syntax': 'exit, quit, end',
         'short': 'exits the application',
         'example': 'exit, quit, end',
         }


    ]

    for i in cmd_list:
        print(c_cmd + '{:>10}: {:<}'.format(c_cmd + c_bold + 'command', i['cmd']) + c_end)
        print('{:>15}: {:<}'.format(c_cmd + 'syntax', c_title + i['syntax']))
        print('{:>15}: {:<}'.format(c_cmd + 'description', c_title + i['short']))
        print('{:>15}: {:<}'.format(c_cmd + 'example', c_title + i['example']))
