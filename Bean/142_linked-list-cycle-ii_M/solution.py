# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    Runtime: 32 ms, faster than 97.27% of Python online submissions for Linked List Cycle II.
    """
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        fast = head.next.next
        slow = head.next
        while fast and fast.next and fast != slow:
            fast = fast.next.next
            slow = slow.next

        if (not fast) or (not fast.next):
            return None
        while head != slow:
            head = head.next
            slow = slow.next
        return head
