'''
python linked list结构
http://blog.csdn.net/qq490691606/article/details/49945287
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    # 初始化
    def __init__(self):
        self.head = None

    # 获取链表长度
    def __len__(self):
        pre = self.head
        l = 0
        while pre:
            l += 1
            pre = pre.next
        return l

    # 添加节点
    def append(self, val):
        node = Node(val)
        if self.head == None:
            self.head = node
        else:
            pre = self.head
            while pre.next:
                pre = pre.next
            pre.next = node

     # 获取节点
    def get(self, idx):
        if len(self) < idx or idx < 0:
            return None
        pre = self.head
        while idx:
            pre = pre.next
            idx -= 1
        return pre

    def set(self, idx, val):
        node = self.get(idx)
        if node:
            node.val = val
        return node

