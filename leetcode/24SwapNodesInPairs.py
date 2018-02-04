#encoding:utf-8
def swapPairs(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head == None or head.next == None:
        return head
    p=dummy=ListNode(0)
    while head and head.next:
        tmp=head.next
        head.next=tmp.next
        tmp.next=head
        p.next=tmp
        p=head
        head=head.next
    return dummy


