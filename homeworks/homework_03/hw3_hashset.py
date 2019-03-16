#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.hw3_hashmap import HashMap


class HashSet(HashMap):

    def get(self, key, default_value=None):
        # TODO достаточно переопределить данный метод
        index = self._get_index(self._get_hash(key))
        if self.array[index] is None:
            return default_value
        else:
            for item in self.array[index]:
                if key == item:
                    return True
            return default_value

    def put(self, key):
        # TODO метод put, нужно переопределить данный метод
        index = self._get_index(self._get_hash(key))
        if self.array[index] is None:
            self.array[index] = [key]
            self.size += 1
        else:
            exists = False
            for item in self.array[index]:
                if key == item:
                    exists = True
                    break
            if not exists:
                self.array[index].append(key)
                self.size += 1
        if self.size * 2 // 3 >= len(self.array):
            self._resize()

    def __len__(self):
        # TODO Возвращает количество Entry в массиве
        return self.size

    def values(self):
        # TODO возвращать итератор значений
        return HashMap.Iterator(self)

    def intersect(self, another_hashset):
        # TODO метод, возвращающий новый HashSet
        #  элементы - пересечение текущего и другого
        new_set = HashSet()
        for key in self.values():
            if key in another_hashset:
                new_set.put(key)

        return new_set

    def __contains__(self, key):
        index = self._get_index(self._get_hash(key))
        if self.array[index] is None:
            return False
        else:
            for item in self.array[index]:
                if key == item:
                    return True
            return False
