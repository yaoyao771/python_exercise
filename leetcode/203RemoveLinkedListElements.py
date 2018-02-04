#encoding:utf-8
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        if head==None:
            return head
        while head!=0:
            if head=val:
                dummp.next=head.next
                dummy=dummy.next
                head=dummy.next
            else:
                dummy=head
                head=head.next
        return p.next