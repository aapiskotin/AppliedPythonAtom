#!/usr/bin/env python
# coding: utf-8

import numpy as np


def simplex_method(a, b, c):
    """
    Почитать про симплекс метод простым языком:
    * https://  https://ru.wikibooks.org/wiki/Симплекс-метод._Простое_объяснение
    Реализацию алгоритма взять тут:
    * https://youtu.be/gRgsT9BB5-8 (это ссылка на 1-ое из 5 видео).

    Используем numpy и, в целом, векторные операции.

    a * x.T <= b
    c * x.T -> max
    :param a: np.array, shape=(n, m)
    :param b: np.array, shape=(n, 1)
    :param c: np.array, shape=(1, m)
    :return x: np.array, shape=(1, m)
    """
    b = b.reshape(-1, 1)
    simplex_table = np.vstack((a, -1 * c))
    simplex_table = np.hstack((simplex_table, np.eye(simplex_table.shape[0]), np.vstack((b, np.zeros((1, 1))))))

    min_indices = [None] * b.shape[0]
    while(np.amin(simplex_table[-1]) < 0):
        pivot_column = np.argmin(simplex_table[-1])
        pivot_row = np.argmin(simplex_table[:-1, -1] / simplex_table[:-1, pivot_column])
        min_indices[pivot_row] = pivot_column
        simplex_table[pivot_row] /= simplex_table[pivot_row, pivot_column]
        simplex_table[:pivot_row] -= simplex_table[:pivot_row, pivot_column].reshape(-1, 1) * simplex_table[pivot_row].reshape(1, -1)
        simplex_table[pivot_row + 1:] -= simplex_table[pivot_row + 1:, pivot_column].reshape(-1, 1) * simplex_table[pivot_row].reshape(1, -1)

    result = np.zeros_like(c)
    for i in range(len(min_indices)):
        if min_indices[i] is not None:
            result[min_indices[i]] = simplex_table[i, -1]

    return result
