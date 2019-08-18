# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    Runtime: 48 ms, faster than 93.29% of Python online submissions for Add Two Numbers.
    """
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        p = res
        carry = 0
        while l1 and l2:
            l1.val += l2.val + carry
            carry = l1.val / 10
            l1.val -= carry * 10
            p.next = l1

            l1 = l1.next
            l2 = l2.next
            p = p.next
            p.next = None

        while l1:
            l1.val += carry
            carry = l1.val / 10
            l1.val -= carry * 10
            p.next = l1

            l1 = l1.next
            p = p.next
            p.next = None

        while l2:
            l2.val += carry
            carry = l2.val / 10
            l2.val -= carry * 10
            p.next = l2

            l2 = l2.next
            p = p.next
            p.next = None

        if carry:
            p.next = ListNode(carry)

        return res.next
