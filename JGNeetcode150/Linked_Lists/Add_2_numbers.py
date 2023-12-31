# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_n = ListNode()
        temp = new_n
        carry = 0
        while l1 and l2:
            next_n = l1.val + l2.val
            if carry > 0:
                next_n += carry
            if next_n >= 10:
                next_n %= 10
                carry = 1
            else:
                carry = 0
            temp.next = ListNode(next_n)
            print(temp)
            temp = temp.next
            l1 = l1.next
            l2 = l2.next
        if l1 is None:
            while l2:
                next_n = l2.val + carry
                if next_n >= 10:
                    next_n %= 10
                    carry = 1
                else:
                    carry = 0
                temp.next = ListNode(next_n)
                temp = temp.next
                l2 = l2.next
            if carry > 0:
                temp.next = ListNode(1)
                return new_n.next
            else:
                return new_n.next
        else:
            while l1:
                next_n = l1.val + carry
                if next_n >= 10:
                    next_n %= 10
                    carry = 1
                else:
                    carry = 0
                temp.next = ListNode(next_n)
                temp = temp.next
                l1 = l1.next
            if carry > 0:
                temp.next = ListNode(1)
                return new_n.next
            else:
                return new_n.next