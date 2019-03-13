from functools import reduce


def make_table(cells):
    max_lengths = max_length_by_column(cells)
    width = reduce((lambda x, y: x + y), max_lengths)
    output = '-' * (len(max_lengths) +
                    2 * len(max_lengths) + len(max_lengths) + 1) + '\n' + '|'
    for i in range(len(cells[0])):
        spacing = (max_lengths[i] - len(cells[0][i])) // 2
        output += ' ' * spacing + cells[0][i] + ' ' * spacing + ' |'
    output += '\n'
    types = column_types(cells[1])
    for i in range(len(cells)):
        output += '|'
        for j in range(len(cells[0])):
            output += ' '
            if types[j] in (int, float):
                output += ' ' * (max_lengths[j] - len(cells[i][j])) \
                          + cells[i][j]
            else:
                output += cells[i][j] + ' ' * \
                          (max_lengths[j] - len(cells[i][j]))
            output += ' |'
        output += '\n'
    output += '-' * (len(max_lengths) + 2 *
                     len(max_lengths) + len(max_lengths) + 1) + '\n' + '|'

    return output


def max_length_by_column(cells):
    max_lengths = []
    for i in range(len(cells[0])):
        max_lengths.append(max(list(map(
            lambda k: len(k), [cells[j][i] for j in range(len(cells))]))))

    return tuple(max_lengths)


def column_types(control_row):
    types = []

    for item in control_row:
        type = int
        for char in item:
            if not (char.isnumeric() or char == '.'):
                type = str
                break
            if char == '.':
                type = float
                break
        types.append(type)

    return tuple(types)
