# -*- coding:utf-8 -*-

# string
# in Python, string is quite cheap
s = "this is a string"

# array, use list in python
arr = list()
arr = [1, 2, 3]

# linked list
class linked_list():
    def __init__(self, val):
        self.val = val
        self.next = None

# binary tree
class binary_tree():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# queue, use list
class queue():
    def __init__(self):
        self.arr = []

    def size(self):
        return arr.length()

    def push(self, val):
        arr.append(val)

    def pop(self):
        return arr.pop(0)

# stack
import collections
stack = collections.deque()

# set
se = set()
se = {1, 3, 2}
se.add(5)
s.remove(5)

# map -> dict
hash_map = {}
hash_map['first'] = 1
hash_map['second'] = 2
pot = hash_map.pop('second')
keys = hash_map.keys()
for key, vale in keys:
    # do sth
    pass


