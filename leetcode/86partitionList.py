'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

For example,
Given 1->4->3->2->5->2 and x = 3,
return 1->2->2->4->3->5.
'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head1 = ListNode(0)
        head2 = ListNode(0)
        Tmp = head
        phead1 = head1
        phead2 = head2
        while Tmp:
            if Tmp.val < x:
                phead1.next = Tmp
                Tmp = Tmp.next
                phead1 = phead1.next
                phead1.next = None
            else:
                phead2.next = Tmp
                Tmp = Tmp.next
                phead2 = phead2.next
                phead2.next = None
        phead1.next = head2.next
        head = head1.next
        return head
