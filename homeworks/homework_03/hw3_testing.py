#!/usr/bin/env python
# coding: utf-8


import os
import shutil


class Requester:
    '''
    Какой-то класс, который умеет делать запросы
     к удаленному серверу
    '''
    def get(self, host, port, filename):
        return "Fail"

    def post(self, host, port, filename, data):
        return False


class MockRequester(Requester):
    def get(self, host, port, filename):
        with open(filename.replace('tmpf/', 'homeworks/homework_03/test_dir/', 1) +
                  '.tmp', "r") as f:
            return f.read()

    def post(self, host, port, filename, data):
        with open(filename.replace('homeworks/homework_03/test_dir', 'tmpf', 1) +
                  '.tmp', "w") as f:
            f.write('\n'.join(data))


class RemoteFileReader(Requester):
    '''
    Класс для работы с файлами на удаленном сервере
    '''
    def __init__(self, host, port):
        self._host = host
        self._port = port

    def read_file(self, filename):
        return super().get(self._host, self._port, filename)

    def write_file(self, filename, data):
        return super().post(self._host, self._port, filename, data)


class OrdinaryFileWorker(RemoteFileReader):
    '''
    Класс, который работает как с локальными
     так и с удаленными файлами
    '''
    def transfer_to_remote(self, filename):
        with open(filename, "r") as f:
            super().write_file(filename, f.readlines())

    def transfer_to_local(self, filename):
        with open(filename, "w") as f:
            f.write(super().read_file(filename))


class MockOrdinaryFileWorker(OrdinaryFileWorker, MockRequester):
    '''
    Необходимо отнаследовать данный класс так, чтобы
     он вместо запросов на удаленный сервер:
      при transfer_to_remote считывал filename
     из локальной директории ./test_dir и сохранял filename.tmp
     в локальной директории ./tmpf
      при transfer_to_local считывал filename.tmp
     из локальной директории ./test_dir и сохранял в filename
     в локальной директории ./tmpf
      при удалении объекта директория ./tmp должна удаляться
      при создании объекта, директория ./tmp должна создаваться
     если еще не создана
    '''
    def __init__(self):
        self._host = 1337
        self._port = 228
        if not os.path.exists('tmpf'):
            os.makedirs('tmpf')

    def transfer_to_remote(self, filename):
        super().transfer_to_remote('homeworks/homework_03/test_dir/' + filename)

    def transfer_to_local(self, filename):
        super().transfer_to_local('tmpf/' + filename)

    def __del__(self):
        shutil.rmtree('tmpf')


class LLNode:
    def __init__(self, value, next_node):
        """
        Entity (or node) for doubly linked list
        :param value: object
        :param next_node: LLEntity
        """
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return "value: {}; next_node: ({})".format(self.value, self.next_node)
