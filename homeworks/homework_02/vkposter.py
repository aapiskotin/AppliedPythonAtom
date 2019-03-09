#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.posts = {}  #post_id:{'host':user_id
                         #         'seen':{user_id_s} }
        self.users = {}  #user_id:{'following:{user_id_s} }

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        self.posts[post_id] = {'host': user_id}
        self.posts[post_id]['seen'] = set()

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        try:
            self.posts[post_id]['seen'].add(user_id)
        except KeyError:
            self.posts[post_id] = {'seen': {user_id}}

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id in self.users:
            self.users[follower_user_id]['following'].add(
                    followee_user_id)
        else:
            self.users[follower_user_id] = {'following': {followee_user_id}}

    def get_recent_posts(self, user_id: int, k: int)-> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        news = []
        for post in self.posts.keys():
            if self.posts[post]['host'] in self.users[user_id]['following']:
                news.append(post)

        return sorted(news, reverse=True)[:k]

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        news = []
        most_popular = []

        for key in self.posts.keys():
            news.append((key, len(self.posts[key]['seen'])))

        news.sort(reverse=True, key=lambda el: el[1])
        print(news)
        return sorted([news[i][0] for i in range(k)], reverse=True)
