"""Handles the IO of the todo program"""
import csv
import json
from os.path import expanduser


def read_csv(path='{}/todo.csv'.format(expanduser("~"))):
    """Reads the CSV file and returns the lines"""
    file = csv.reader(open(path, 'r'))
    return [line for line in file]

def read_json(path='{}/todo.json'.format(expanduser("~"))):
    """Reads the json file and returns its objects"""
    return json.load(open(path, 'r'))

if __name__ == '__main__':
    print(read_json())
