#!/usr/bin/env python
# coding: utf-8


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param : input_string строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''

    rpn = []
    oper_stack = []

    input_string = input_string.strip()
    is_valid = True
    i = 0
    for i in range(len(input_string)):
        if input_string[i].isnumeric() or input_string == '.':
            break
        if input_string[i] in ('(', ' ', '+', '-', '*', '/'):
            continue
        else:
            return None
    while(i < len(input_string)):
        if input_string[i] == ' ':
            is_valid = False
            while(i < len(input_string) and not
                    (input_string[i].isnumeric() or
                     input_string[i] == '.')):
                print(input_string[i], is_valid)
                if input_string[i] in ('-', '+', '/', '*'):
                    is_valid = True
                i += 1
            if not is_valid:
                return None
        i += 1

    input_string = input_string.replace(' ', '')
    if input_string.find('+') != -1 or input_string.find('-') != -1:
        input_string = remove_multiple_plus_minus(input_string)
    if input_string is None:
        return None

    i = 0
    while (i < len(input_string)):
        if input_string[i] == '(':
            oper_stack.append(input_string[i])
        elif input_string[i] == ')':
            if '(' in oper_stack and len(rpn) != 0:
                while(oper_stack[-1] != '('):
                    rpn.append(oper_stack.pop())
                oper_stack.pop()
            else:
                return None
        elif input_string[i] == '+':
            if i == 0:
                i += 1
                continue
            while(len(oper_stack) != 0 and oper_stack[-1] != '('):
                rpn.append(oper_stack.pop())
            oper_stack.append(input_string[i])
        elif input_string[i] == '-':
            if i != 0 and input_string[i - 1].isnumeric():
                while(len(oper_stack) != 0 and oper_stack[-1] != '('):
                    rpn.append(oper_stack.pop())
                oper_stack.append(input_string[i])
            else:
                oper_stack.append('_')  # Унарный минус
        elif input_string[i] in ('*', '/'):
            if i != 0 and input_string[i - 1].isnumeric() or \
                    input_string[i - 1] == ')':
                while(len(oper_stack) != 0 and
                        oper_stack[-1] in ('*', '/')):
                    rpn.append(oper_stack.pop())
                oper_stack.append(input_string[i])
            else:
                return None
        elif input_string[i].isnumeric() or input_string[i] == '.':
            number = ''
            while(i < len(input_string) and input_string[i].isnumeric()):
                number += input_string[i]
                i += 1
            if i < len(input_string) and input_string[i] == '.':
                number += '.'
                i += 1
            while(i < len(input_string) and input_string[i].isnumeric()):
                number += input_string[i]
                i += 1
            if i < len(input_string) and input_string[i] == '.':
                return None
            rpn.append(float(number))
            i -= 1
        else:
            return None
        i += 1

    rpn.extend(oper_stack[::-1])
    if '(' in rpn:
        return None

    calc_stack = []
    for token in rpn:
        if isinstance(token, float):
            calc_stack.append(token)
        elif len(calc_stack) > 0:
            if token == '*':
                x = calc_stack.pop()
                y = calc_stack.pop()
                calc_stack.append(y * x)
            elif token == '+':
                x = calc_stack.pop()
                y = calc_stack.pop()
                calc_stack.append(y + x)
            elif token == '-':
                x = calc_stack.pop()
                y = calc_stack.pop()
                calc_stack.append(y - x)
            elif token == '/':
                x = calc_stack.pop()
                y = calc_stack.pop()
                if y == 0:
                    return None
                calc_stack.append(y / x)
            elif token == '_':  # Унарный минус
                calc_stack.append(- calc_stack.pop())
        else:
            return None

    if len(calc_stack) != 1:
        return None
    return calc_stack.pop()


def remove_multiple_plus_minus(input_string):

    i = 0
    while (i < len(input_string)):
        sequence = ''
        is_plus = True
        j = 0
        while(input_string[i + j] in ('+', '-')):
            sequence += input_string[i + j]
            if input_string[i + j] == '-':
                is_plus = not is_plus
            j += 1
            if i + j >= len(input_string):
                return None
        token = '+' if is_plus else '-'
        if len(sequence) != 0:
            input_string = input_string.replace(sequence, token)
        i += 1

    return input_string
