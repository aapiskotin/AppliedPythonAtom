import sys


def parse_json(json_object):
    columns = tuple(json_object[0].keys())

    cells = [len(columns)]
    for item in json_object:
        row = list(item.values())
        if set(row.keys) != set(columns):
            print('Формат не валиден 1jtt')
            sys.exit()
        if len(row) != len(columns):
            print('Формат не валиден 2jtt')
            sys.exit()
        cells.append(row)

    return cells
