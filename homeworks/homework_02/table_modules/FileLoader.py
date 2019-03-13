import sys
import json
from exceptions import *
from json import JSONDecodeError


class FileLoader:

    def __init__(self, filename):
        self.filename = filename

    def load_all(self):
        try:
            fh = open(self.filename, 'r', encoding='utf8')
        except UnicodeDecodeError:
            fh = open(self.filename, 'r', encoding='cp1251')
        except FileNotFoundError:
            raise FileNotFoundError('Файл не валиден')


        try:
            table = json.load(fh)
            if len(table) < 1:
                raise FormatError('Формат не валиден')
            self.format = 'json'
            fh.close()
        except JSONDecodeError:
            table = fh.read()
            self.format = 'tsv'
            if len(table) == 0:
                raise FormatError('Формат не валиден')
            fh.close()

        return table

    def is_json(self):
        if self.format == 'json':
            return True
        else:
            return False

    def is_tsv(self):
        if self.format == 'tsv':
            return True
        else:
            return False
