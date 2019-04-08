#!/usr/bin/env python
# coding: utf-8


import numpy as np


class CSRMatrix:
    """
    CSR (2D) matrix.
    Here you can read how CSR sparse matrix works: https://en.wikipedia.org/wiki/Sparse_matrix
    """
    def __init__(self, init_matrix_representation):
        """
        :param init_matrix_representation: can be usual dense matrix
        or
        (row_ind, col, data) tuple with np.arrays,
            where data, row_ind and col_ind satisfy the relationship:
            a[row_ind[k], col_ind[k]] = data[k]
        """
        if isinstance(init_matrix_representation, tuple) and len(init_matrix_representation) == 3:
            self.A = np.array(init_matrix_representation[2])
            self.IA = np.zeros(len(init_matrix_representation[0]) + 1, dtype=int)
            self.JA = np.array(init_matrix_representation[1])
            self._shape = (self.IA.shape[0] - 1, max(self.JA))
            for i in range(len(init_matrix_representation[0])):
                self.IA[init_matrix_representation[0][i] + 1:] += 1

        elif isinstance(init_matrix_representation, np.ndarray):
            init_a = init_matrix_representation
            self.A = []
            self.IA = [0]
            self.JA = []
            self._shape = init_a.shape
            for i in range(init_a.shape[0]):
                self.IA.append(self.IA[-1])
                for j in range(init_a.shape[1]):
                    if init_a[i, j] != 0:
                        self.A.append(init_a[i, j])
                        self.IA[-1] += 1
                        self.JA.append(j)
            self.A = np.array(self.A)
            self.IA = np.array(self.IA)
            self.JA = np.array(self.JA)

        else:
            raise ValueError

    def get_item(self, i, j):
        """
        Return value in i-th row and j-th column.
        Be careful, i and j may have invalid values (-1 / bigger that matrix size / etc.).
        """
        self._assert_i_j(i, j)

        for k in range(self.IA[i], self.IA[i + 1]):
            if self.JA[k] == j:
                return self.A[k]
        return 0

    def set_item(self, i, j, value):
        """
        Set the value to i-th row and j-th column.
        Be careful, i and j may have invalid values (-1 / bigger that matrix size / etc.).
        """
        self._assert_i_j(i, j)

        if self.IA[i] == self.IA[i + 1]:
            self.JA = np.insert(self.JA, self.IA[i], j)
            self.A = np.insert(self.A, self.IA[i], value)
            self.IA[i + 1:] += 1
        for k in range(self.IA[i], self.IA[i + 1]):
            if j > self.JA[k]:
                self.JA = np.insert(self.JA, k + 1, j)
                self.A = np.insert(self.A, k + 1, value)
                self.IA[i + 1:] += 1
                break

    def to_dense(self):
        """
        Return dense representation of matrix (2D np.array).
        """
        dense = np.zeros(self._shape)
        for i in range(1, self.IA.shape[0]):
            for k in range(self.IA[i - 1], self.IA[i]):
                dense[i - 1, self.JA[k]] = self.A[k]

        return dense

    def _assert_i_j(self, i, j):
        assert i < self.IA.shape[0]
        assert i >= 0
        assert j >= 0
