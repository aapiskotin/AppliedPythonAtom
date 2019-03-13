import sys

from table_modules.TsvToTable import *
from table_modules.JsonToTable import *
from table_modules.FileLoader import *
from table_modules.TableDecorator import *

if __name__ == '__main__':
    filename = sys.argv[1]

table_loader = FileLoader(filename)
table = table_loader.load_all()

if table_loader.is_json():
    table = parse_json(table)
elif table_loader.is_tsv():
    table = parse_tsv(table)

print(make_table(table))
