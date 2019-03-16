#!/usr/bin/env python
# coding: utf-8

from homeworks.homework_03.homework_modules.LinkedListIterator import LinkedListIterator
from collections import deque


def revert_linked_list(head):
    """
    A -> B -> C should become: C -> B -> A
    :param head: LLNode
    :return: new_head: LLNode
    """
    if head is None:
        return None
    if head.next_node is None:
        return head

    tmp = deque(maxlen=2)
    for node in LinkedListIterator(head):
        print(node.__repr__())
        if len(tmp) < 2:
            if len(tmp) == 1:
                tmp[0].next_node = None
            tmp.append(node)
            continue
        tmp[1].next_node = tmp[0]
        tmp.append(node)
    node = node.next_node
    if len(tmp) == 1:
        node.next_node = tmp[0]
        tmp[0].next_node = None
        return node
    else:
        tmp[1].next_node = tmp[0]
        node.next_node = tmp[1]
        return node
