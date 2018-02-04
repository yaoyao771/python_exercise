#encoding:utf-8
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        tmp=dummy=ListNode(0)
        for i in range(k):
            p(i)=head.next
            head=head.next

