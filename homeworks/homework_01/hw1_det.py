#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''
    for row in list_of_lists:
        if len(row) != len(list_of_lists):
            return None

    import copy
    a = copy.deepcopy(list_of_lists)
    for i in range(len(a) - 1):
        if a[i][i] == 0:
            for j in range(i + 1, len(a) - 1):
                if a[j][i] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
        for k in range(i + 1, len(a)):
            row_multiplier = a[k][i] / a[i][i]
            for j in range(len(a)):
                a[k][j] -= a[i][j] * row_multiplier

    det = 1
    for i in range(len(a)):
        det *= a[i][i]
    print(det)

    return det
