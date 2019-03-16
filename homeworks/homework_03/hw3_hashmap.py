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
            return self.key == other.get_key()

        def get_item(self):
            return (self.key, self.value)

        def __str__(self):
            return self.key + ': ' + self.value

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
            return default_value

    def put(self, key, value):
        index = self._get_index(self._get_hash(key))
        if self.array[index] is None:
            self.array[index] = [HashMap.Entry(key, value)]
            self.size += 1
        else:
            exists = False
            for i in range(len(self.array[index])):
                if self.array[index][i].get_key() == key:
                    self.array[index][i] = HashMap.Entry(key, value)
                    exists = True
                    break
            if not exists:
                self.array[index].append(HashMap.Entry(key, value))
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
            while(self.bucket_i < len(self.hash.array)):
                if self.hash.array[self.bucket_i] is None:
                    self.bucket_i += 1
                elif self.chain_i < len(self.hash.array[self.bucket_i]):
                    cur_entry = self.hash.array[self.bucket_i][self.chain_i]
                    self.chain_i += 1
                    return cur_entry.get_value()
                else:
                    self.bucket_i += 1
                    self.chain_i = 0
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
            while(self.bucket_i < len(self.hash.array)):
                if self.hash.array[self.bucket_i] is None:
                    self.bucket_i += 1
                elif self.chain_i < len(self.hash.array[self.bucket_i]):
                    cur_entry = self.hash.array[self.bucket_i][self.chain_i]
                    self.chain_i += 1
                    return cur_entry.get_key()
                else:
                    self.bucket_i += 1
                    self.chain_i = 0
            raise StopIteration

    def keys(self):
        return HashMap.KeysIterator(self)

    class ItemIterator:
        def __init__(self, hashmap):
            self.bucket_i = 0
            self.chain_i = 0
            self.hash = hashmap

        def __iter__(self):
            return self

        def __next__(self):
            while(self.bucket_i < len(self.hash.array)):
                if self.hash.array[self.bucket_i] is None:
                    self.bucket_i += 1
                elif self.chain_i < len(self.hash.array[self.bucket_i]):
                    cur_entry = self.hash.array[self.bucket_i][self.chain_i]
                    self.chain_i += 1
                    return cur_entry.get_item()
                else:
                    self.bucket_i += 1
                    self.chain_i = 0
            raise StopIteration

    def items(self):
        return HashMap.ItemIterator(self)

    def _resize(self):
        old_array = self.array
        self.array = [None] * 2 * len(self.array)
        self.size = 0
        for bucket in old_array:
            if bucket is None:
                continue
            for entry in bucket:
                self.put(*entry.get_item())

    def __str__(self):
        return '{' + ', '.join(list(self.items)) + '}'

    def __contains__(self, item):
        index = self._get_index(self._get_hash(item))
        if self.array[index] is None:
            return False
        else:
            for entry in self.array[index]:
                if entry.get_key() == item:
                    return True
            return False
