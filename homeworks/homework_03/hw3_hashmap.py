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
            return (self.key, self.value) == other

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
                if entry_tuple is None:
                    break
                self.put(*entry_tuple)
        else:
            index = self._get_index(self._get_hash(key))
            if self.array[index] is None:
                self.array[index] = [HashMap.Entry(key, value)]
            else:
                for i in range(len(self.array[index])):
                    if self.array[index][i].get_key() == key:
                        self.array[index][i] = HashMap.Entry(key, value)
                        break
            self.size += 1
            if self.size * 2 // 3 >= len(self.array):
                self._resize()

    def __len__(self):
        return self.size

    def _get_hash(self, key):
        return hash(key)

    def _get_index(self, hash_value):
        return hash_value % len(self.array)

    class ValuesIterator:
        def __init__(self, hashmap):
            self.bucket_i = 0
            self.chain_i = 0
            self.hash = hashmap

        def __iter__(self):
            return self

        def __next__(self):
            if self.bucket_i < len(self.hash.array):
                if self.hash.array[self.bucket_i] is None:
                    self.bucket_i += 1
                elif self.chain_i < len(self.hash.array[self.bucket_i]):
                    self.chain_i += 1
                    cur_entry = self.hash.array[self.bucket_i][self.chain_i - 1]
                    return cur_entry.get_value()
                else:
                    self.bucket_i += 1
                    self.chain_i = 0
            else:
                raise StopIteration


    def values(self):
        return HashMap.ValuesIterator(self)

    class KeysIterator:
        def __init__(self, hashmap):
            self.bucket_i = 0
            self.chain_i = 0
            self.hash = hashmap

        def __iter__(self):
            return self

        def __next__(self):
            if self.bucket_i < len(self.hash.array):
                if self.hash.array[self.bucket_i] is None:
                    self.bucket_i += 1
                elif self.chain_i < len(self.hash.array[self.bucket_i]):
                    self.chain_i += 1
                    cur_entry = self.hash.array[self.bucket_i][self.chain_i - 1]
                    return cur_entry.get_key()
                else:
                    self.bucket_i += 1
                    self.chain_i = 0
            else:
                raise StopIteration

    def keys(self):
        return HashMap.KeysIterator(self)

    class ItemIterator:
        def __init__(self, hashmap):
            self.bucket_i = 0
            self.chain_i = 0
            self.hashmap = hashmap

        def __iter__(self):
            return self

        def __next__(self):
            if self.bucket_i < len(self.hashmap.array):
                if self.hashmap.array[self.bucket_i] is None:
                    self.bucket_i += 1
                elif self.chain_i < len(self.hashmap.array[self.bucket_i]):
                    self.chain_i += 1
                    cur_entry = self.hashmap.array[self.bucket_i][self.chain_i - 1]
                    return (cur_entry.get_key(), cur_entry.get_value())
                else:
                    self.bucket_i += 1
                    self.chain_i = 0
            else:
                raise StopIteration

    def items(self):
        return HashMap.ItemIterator(self)

    def _resize(self):
        new_array = [None] * 2 * len(self.array)
        for bucket in self.array:
            if bucket is None:
                continue
            key = bucket[0].get_key()
            index = self._get_index(self._get_hash(key))
            if new_array[index] is None:
                new_array[index] = bucket
            else:
                new_array[index].extend(bucket)

        self.array = new_array

    def __str__(self):
        return "buckets: " + str(self.array) + ", items: " + str(list(self.items()))

    def __contains__(self, item):
        if self.array[self._get_index(self._get_hash)] is None:
            return False
        else:
            return True
