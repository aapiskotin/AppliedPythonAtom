#!/usr/bin/env python
# coding: utf-8


class HashMap:
    '''
    Давайте сделаем все объектненько,
     поэтому внутри хешмапы у нас будет Entry
    '''
    class Entry:
        def __init__(self, key, value):
            '''
            Сущность, которая хранит пары ключ-значение
            :param key: ключ
            :param value: значение
            '''
            self.key = key
            self.value = value

        def get_key(self):
            return self.key

        def get_value(self):
            return self.value

        def __eq__(self, other):
            return self == other

    def __init__(self, bucket_num=64):
        '''
        Реализуем метод цепочек
        :param bucket_num: число бакетов при инициализации
        '''
        self.array = [None] * bucket_num
        self.size = 0

    def get(self, key, default_value=None):
        index = self._get_index(self._get_hash(key))
        if self.array[index] is None:
            return default_value
        else:
            for entry in self.array[index]:
                if entry.get_key() == key:
                    return entry.get_value()

    def put(self, key, value):
        if isinstance(key, HashMap):
            for entry_tuple in key.items():
                self.put(*entry_tuple)
        index = self._get_index(self._get_hash(key))
        if self.array[index] is None:
            self.array[index] = [Entry(key, value)]
        else:
            for i in range(len(self.array[index])):
                if self.array[index][i].get_key() == key:
                    self.array[index].pop(i)
                    break
            self.array[index].append(Entry(key, value))
        self.size += 1
        if self.size * 2 // 3 >= len(self.array):
            self._resize()

    def __len__(self):
        return self.size

    def _get_hash(self, key):
        if isinstance(key, (int, float)):
            return int(key)
        elif isinstance(key, str):
            hash_func = 0
            for char in key:
                hash_func += ord(char)
            return hash_func
        else:
            raise TypeError

    def _get_index(self, hash_value):
        return hash_value % len(self.array)

    class ValuesIterator:
        def __init__(self):
            self.bucket_i = 0
            self.chain_i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.bucket_i < len(self.array):
                if self.array[self.bucket_i] is None:
                    self.bucket_i += 1
                elif self.chain_i < len(self.array[self.bucket_i]):
                    self.chain_i += 1
                    cur_entry = self.array[self.bucket_i][self.chain_i - 1]
                    return cur_entry.get_value()
                else:
                    self.bucket_i += 1
                    self.chain_i = 0
            else:
                raise StopIteration


    def values(self):
        return ValuesIterator()

    class KeysIterator:
        def __init__(self):
            self.bucket_i = 0
            self.chain_i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.bucket_i < len(self.array):
                if self.array[self.bucket_i] is None:
                    self.bucket_i += 1
                elif self.chain_i < len(self.array[self.bucket_i]):
                    self.chain_i += 1
                    cur_entry = self.array[self.bucket_i][self.chain_i - 1]
                    return cur_entry.get_key()
                else:
                    self.bucket_i += 1
                    self.chain_i = 0
            else:
                raise StopIteration

    def keys(self):
        return KeysIterator()

    class ItemIterator:
        def __init__(self):
            self.bucket_i = 0
            self.chain_i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.bucket_i < len(self.array):
                if self.array[self.bucket_i] is None:
                    self.bucket_i += 1
                elif self.chain_i < len(self.array[self.bucket_i]):
                    self.chain_i += 1
                    cur_entry = self.array[self.bucket_i][self.chain_i - 1]
                    return (cur_entry.get_key(), cur_entry.get_value())
                else:
                    self.bucket_i += 1
                    self.chain_i = 0
            else:
                raise StopIteration

    def items(self):
        return ItemIterator()

    def _resize(self):
        self.array.extend([None] * len(self.array))

    def __str__(self):
        return "buckets: " + str(self.array) + ", items: " + str(list(self.items()))

    def __contains__(self, item):
        if self.array[self._get_index(self._get_hash)] is None:
            return False
        else:
            return True
