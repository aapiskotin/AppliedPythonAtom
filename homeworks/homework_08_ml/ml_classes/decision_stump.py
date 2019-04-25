#!/usr/bin/env python
# coding: utf-8

import numpy as np


class DecisionStumpRegressor:
    '''
    Класс, реализующий решающий пень (дерево глубиной 1)
    для регрессии. Ошибку считаем в смысле MSE
    '''

    def __init__(self):
        '''
        Мы должны создать поля, чтобы сохранять наш порог th и ответы для
        x <= th и x > th
        '''
        self._th = None
        self._y1 = None
        self._y2 = None

    def fit(self, X, y):
        '''
        метод, на котором мы должны подбирать коэффициенты th, y1, y2
        :param X: массив размера (1, num_objects)
        :param y: целевая переменная (1, num_objects)
        :return: None
        '''
        self._th = np.mean(X)
        mse_s = []
        params = []
        for i in range(len(X) - 1):
            th = np.mean(X[i:i + 1])
            y_pred = np.zeros(size=y.shape)
            y1 = np.mean(y[:i + 1])
            y_pred[:i + 1] = y1
            y2 = np.mean(y[i + 1:])
            y_pred[i + 1:] = y2
            mse = np.sum((y - y_pred) ** 2) / len(y)
            mse_s.append(mse)
            params.append((th, y1, y2))

        self._th, self._y1, self._y2 = params[np.argmin(mse_s)]

    def predict(self, X):
        '''
        метод, который позволяет делать предсказания для новых объектов
        :param X: массив размера (1, num_objects)
        :return: массив, размера (1, num_objects)
        '''
        y_pred = []
        for x in X:
            if x > th:
                y_pred.append(self._y2)
            else:
                y_pred.append(self._y1)

        return y_pred
