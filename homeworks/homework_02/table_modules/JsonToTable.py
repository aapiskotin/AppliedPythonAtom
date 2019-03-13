import sys
from exceptions import *


def parse_json(json_object):
    columns = tuple(json_object[0].keys())

    cells = [len(columns)]
    for item in json_object:
        row = list(item.values())
        if set(row.keys) != set(columns):
            raise FormatError('Формат не валиден')
            sys.exit()
        if len(row) != len(columns):
            raise FormatError('Формат не валиден')
            sys.exit()
        cells.append(row)

    return cells
