#!/usr/bin/env python
# coding: utf-8

from multiprocessing import Pool
import os


def word_count_inference(path_to_dir):
    '''
    Метод, считающий количество слов в каждом файле из директории
    и суммарное количество слов.
    Слово - все, что угодно через пробел, пустая строка "" словом не считается,
    пробельный символ " " словом не считается. Все остальное считается.
    Решение должно быть многопроцессным. Общение через очереди.
    :param path_to_dir: путь до директории с файлами
    :return: словарь, где ключ - имя файла, значение - число слов +
        специальный ключ "total" для суммы слов во всех файлах
    '''
    files = list(os.listdir(path_to_dir))
    counts = []
    with Pool(len(files)) as proc:
        counts = proc.map(count_words, list(map(lambda k: path_to_dir + '/' + k, files)))

    result_dict = dict(zip(files, counts))
    result_dict['total'] = sum(counts)

    return result_dict


def count_words(path_to_file):
    with open(path_to_file, 'r') as f:
        count = 0
        for line in list(filter(lambda k: k != '\n', f.readlines())):
            count += len(line.split(' '))

        return count
