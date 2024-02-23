from pathlib import Path
import pickle


def load_contacts():
    if Path.is_file(Path('contacts.txt')):
        with open('contacts.txt', 'rb') as fh:
            return pickle.load(fh)
    else:
        print('no contacts')
        return []
