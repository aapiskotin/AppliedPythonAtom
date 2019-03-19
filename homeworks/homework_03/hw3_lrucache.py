#!/usr/bin/env python
# coding: utf-8
import time


class LRUCacheDecorator:

    def __init__(self, maxsize, ttl):
        '''
        :param maxsize: максимальный размер кеша
        :param ttl: время в млсек, через которое кеш
                    должен исчезнуть
        '''
        self.maxsize = maxsize
        self.ttl = ttl
        self.cache = []

    def __call__(self, function):

        def _decorated_f(*args, **kwargs):
            print(len(self.cache), self.cache)
            for i in range(len(self.cache)):
                if (args, kwargs) == self.cache[i]['arguments']:
                    if self.ttl is not None and time.time() - self.cache[i]['last_use_time'] > self.ttl / 1000:
                        self.cache[i]['result'] = function(*args, **kwargs)
                    self.cache[i]['last_use_time'] = time.time()
                    return self.cache[i]['result']

            result = function(*args, **kwargs)
            new_line = {'arguments': (args, kwargs), 'last_use_time': time.time(), 'result': result}
            if len(self.cache) < self.maxsize:
                self.cache.append(new_line)
            else:
                self.cache[self.cache.index(min(self.cache, key=lambda k: k['last_use_time']))] = new_line

            return result

        return _decorated_f
