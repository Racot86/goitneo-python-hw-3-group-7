from collections import UserDict


class Record:
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.address = ''
        self.birth_date = ''
        self.favorite = False
        self.note = ''
        self.email = ''


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record

    def records(self):
        return self.data
