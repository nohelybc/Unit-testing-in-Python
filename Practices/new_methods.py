import glob
import logging
import os


def verify_data():
    id = '171368'
    name = 'name001'
    if id.isdigit() and name:
        print('id and host are valid')
    else:
        print('id and host are invalid')


def last_file():
    path = '/local/path/'
    updated_file = max(glob.iglob(f'{path}*.csv'), key=os.path.getctime)

    read_file(updated_file)
    return updated_file


def read_file(path):
    auth = 0
    try:
        if content := [line.rstrip('\n') for line in open(path)]:
            auth = compare_files(content)
        else:
            logging.debug('File is empty')
        return auth
    except FileNotFoundError as e:
        logging.error('File not found')
        raise FileNotFoundError from e


def compare_files(content):
    stringss = ['Hello world', 'sending message', 'No Error']
    return all(any(s in x for x in content) for s in stringss)


def set_message():
    condition_1 = 1
    condition_2 = 0
    message = 'This is the default message'
    if condition_1:
        message = 'This is the message if condition_1 is true'
    elif condition_2:
        message = 'This is the message if condition_2 is true'
    return message
