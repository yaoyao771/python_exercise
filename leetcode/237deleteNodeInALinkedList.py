class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node == None:
            return
        dummy = node.next
        if dummy != None:
            node.val = dummy.val
            node.next = dummy.next
        else:
            node = None
