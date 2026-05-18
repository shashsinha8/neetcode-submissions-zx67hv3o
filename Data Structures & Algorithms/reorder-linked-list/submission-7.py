# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head.next: 
            return

        # find middle
        slow, fast = head, head
        prev = None
        while fast and fast.next: 
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        # reverse second half
        prev = None
        while slow: 
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        

        # merge both lists
        l1 = head
        l2 = prev
        dummy = ListNode()
        curr = dummy
        
        flag = True
        while l1 and l2:
            if flag: 
                curr.next = l1
                l1 = l1.next
                curr = curr.next
                flag = False
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next
                flag = True

        if l1: 
            curr.next = l1
        elif l2: 
            curr.next = l2
        curr = dummy.next

        # return dummy.next