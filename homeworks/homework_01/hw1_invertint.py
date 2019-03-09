#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''
    is_negative = False
    if number < 0:
        number = - number
        is_negative = True

    list_reversed = list(str(number))[::-1]

    string_reversed = ''
    for digit in list_reversed:
        string_reversed += digit

    if is_negative:
        return - int(string_reversed)
    else:
        return int(string_reversed)
