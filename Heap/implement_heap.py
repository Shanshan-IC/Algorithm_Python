# -*- coding:utf-8 -*-

# 实现heapclass

class Heap():
    """
    先进先出实现队列
    """
    def __init__(self, size):
        self.size = size
        self.