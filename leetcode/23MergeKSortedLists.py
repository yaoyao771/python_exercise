#encoding:utf-8
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        l1 = self.mergeKLists(lists[:len(lists) / 2])
        l2 = self.mergeKLists(lists[len(lists) / 2:])
        head = self.mergeTwoLists(l1, l2)
        return head

    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        p = ListNode(0)
        dummy = p
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            elif l1.val > l2.val:
                p.next = l2
                l2 = l2.next
                p = p.next
        if l1 is None:
            p.next = l2
        else:
            p.next = l1
        return dummy.next
