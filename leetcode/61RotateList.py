#encoding:utf-8
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        headnode = ListNode(0)
        headnode.next = head
        temp = head
        for i in range(k):
            head = head.next
        tmp = head.next
        head.next = null
        head.node.next = tmp
        while tmp.next:
            tmp = tmp.next
        tmp.next = temp
        return headnode.next
