from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        add = 0
        next_val = 0

        next_val = l1.val + l2.val
        if next_val >= 10:
            add = 1
            next_val = next_val % 10
        
        root = ListNode(next_val)
        iter = root

        l1 = l1.next
        l2 = l2.next

        while True:
            if (l1 != None) & (l2 != None):

                next_val = l1.val + l2.val + add
                add = 0
                if next_val >= 10:
                    add = 1
                    next_val = next_val % 10

                root.next = ListNode(next_val)

                l1 = l1.next
                l2 = l2.next
                root = root.next
            elif (l1 != None):
                next_val = l1.val + add
                add = 0
                if next_val >= 10:
                    add = 1
                    next_val = next_val % 10
                
                root.next = ListNode(next_val)

                l1 = l1.next
                root = root.next
            elif (l2 != None):
                next_val = l2.val + add
                add = 0
                if next_val >= 10:
                    add = 1
                    next_val = next_val % 10
                
                root.next = ListNode(next_val)

                l2 = l2.next
                root = root.next
            else:
                if add == 1:
                    root.next = ListNode(1)
                return iter
        





        

            