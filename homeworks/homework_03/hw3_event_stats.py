#!/usr/bin/env python
# coding: utf-8
from collections import deque
from collections import namedtuple
from collections import Counter


class TEventStats:
    FIVE_MIN = 300

    def __init__(self):
        self.events_list = deque()
        self.event = namedtuple('Event', 'user_id time')

    def register_event(self, user_id, time):
        """
        Этот метод регистрирует событие активности пользователя.
        :param user_id: идентификатор пользователя
        :param time: время (timestamp)
        :return: None
        """
        self.events_list.append(self.event(user_id=user_id, time=time))

    def query(self, count, time):
        """
        Этот метод отвечает на запросы.
        Возвращает количество пользователей, которые за последние 5 минут
        (на полуинтервале времени (time - 5 min, time]), совершили ровно count действий
        :param count: количество действий
        :param time: время для рассчета интервала
        :return: activity_count: int
        """
        start_time = time - 300
        start_i = 0
        for i in range(len(self.events_list)):
            if self.events_list[i].time > start_time:
                start_i = i
                break

        end_i = 0
        for i in range(len(self.events_list) - 1, -1, -1):
            if self.events_list[i].time <= time:
                end_i = i
                break

        counted = Counter(list(map(lambda k: k[0], list(self.events_list)[start_i:end_i + 1])))
        result = 0
        for value in counted.values():
            if value == count:
                result += 1

        return result
