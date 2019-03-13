import sys


def parse_tsv(raw_string):
    cells = raw_string.split('\n')

    for i in range(len(cells)):
        cells[i] = cells[i].split('\t')

    validate_tsv(cells)
    return cells


def validate_tsv(cells):
    for row in cells:
        if len(row) != len(cells[0]):
            print('Формат не валиден 1ttt')
            sys.exit()
