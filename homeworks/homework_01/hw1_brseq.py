#!/usr/bin/env python
# coding: utf-8


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''

    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for char in input_string:
        if char in brackets.keys():
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            elif brackets[stack[-1]] == char:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False
