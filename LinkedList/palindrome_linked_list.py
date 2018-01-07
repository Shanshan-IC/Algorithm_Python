"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    @param: head: A ListNode.
    @return: A boolean.
    """

    def isPalindrome(self, head):
        copyed = head
        rever = self.reverse(copyed)
        printlist(rever)
        printlist(head)
        while head:
            if head.val != rever.val:
                return False
            head = head.next
            rever = rever.next
        return True

    def reverse(self, head):
        cur = None
        while head:
            tmp = head.next
            head.next = cur
            cur = head
            head = tmp
        return cur

def printlist(head):
    while head:
        print(head.val, )
        head = head.next

head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(0)
head.next.next.next.next.next = ListNode(1)

Solution().isPalindrome(head)