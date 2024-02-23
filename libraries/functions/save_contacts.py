import pickle
import os


def save_contacts(data):
    if len(data) > 0:
        with open('contacts.txt', 'wb') as fh:
            pickle.dump(data, fh)
    else:
        if os.path.exists("contacts.txt"):
            os.remove("contacts.txt")
