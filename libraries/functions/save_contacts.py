import pickle


def save_contacts(data):
    if len(data) > 0:
        with open('contacts.txt', 'wb') as fh:
            pickle.dump(data, fh)
