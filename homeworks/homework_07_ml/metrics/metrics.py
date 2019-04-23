#!/usr/bin/env python
# coding: utf-8


import numpy as np


def logloss(y_true, y_pred):
    """
    logloss
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    eps = 1e-10
    y_pred = np.clip(y_pred, eps, 1 - eps)

    return - 1 / len(y_true) * np.sum(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))


def accuracy(y_true, y_pred):
    """
    Accuracy
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    return np.sum(np.equal(y_true, y_pred)) / len(y_pred)


def presicion(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    return np.sum(y_pred * y_true) / np.sum(y_pred)


def recall(y_true, y_pred):
    """
    presicion
    :param y_true: vector of truth (correct) class values
    :param y_hat: vector of estimated class values
    :return: loss
    """
    return np.sum(y_pred * y_true) / np.sum(y_true)


def roc_auc(y_true, y_pred):
    """
    roc_auc
    :param y_true: vector of truth (correct) target values
    :param y_hat: vector of estimated probabilities
    :return: loss
    """
    n1 = np.sum(y_true)
    n0 = len(y_true) - n1

    auc = 0
    fpr = 0
    tpr = 0
    for i in np.argsort(-y_pred):
        if y_true[i] == 0:
            auc += tpr / n0
            fpr += 1 / n0
        else:
            tpr += 1 / n1

    return auc
