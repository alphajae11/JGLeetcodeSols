# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def iterreverse(self, head: Optional[ListNode], store: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return ListNode(head.val, store)
        else:
            store = ListNode(head.val, store)
            return self.iterreverse(head.next, store)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        else:
            return self.iterreverse(head, None)