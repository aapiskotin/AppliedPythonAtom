#!/usr/bin/env python
# coding: utf-8


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''
    if not isinstance(source_dict, dict):
        return None

    new_dict = {}
    for key in source_dict.keys():
        new_dict = invert_rec(new_dict, source_dict[key], key)

    return new_dict


def invert_rec(my_dict, my_item, key):
    if isinstance(my_item, (list, tuple, set)):
        for item in my_item:
            if isinstance(item, (list, tuple, set)):
                my_dict = invert_rec(my_dict, item, key)
            else:
                my_dict = write_dict(my_dict, item, key)
    else:
        my_dict = write_dict(my_dict, my_item, key)

    return my_dict


def write_dict(my_dict, item, key):
    if item in my_dict:
        if isinstance(my_dict[item], list):
            my_dict[item].append(key)
        else:
            my_dict[item] = [my_dict[item], key]
    else:
        my_dict[item] = key

    return my_dict
