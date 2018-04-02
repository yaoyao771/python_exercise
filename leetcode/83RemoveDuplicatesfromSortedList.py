'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.


'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        cur = head
        dummy = ListNode('#')
        dummy.next = head
        pre = dummy
        cur = dummy.next
        while cur != None:
            while cur.next != None and cur.val == cur.next.val:
                cur = cur.next
            if pre.val == cur.val:
                pre.next = cur.next
                pre = pre.next
                cur = cur.next

            else:
                pre.next = cur
                pre = pre.next
                cur = cur.next
        return dummy.next
