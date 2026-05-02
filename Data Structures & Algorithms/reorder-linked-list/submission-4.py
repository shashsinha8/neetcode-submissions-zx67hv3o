# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find mid
        slow = fast = head
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

        curr = slow.next
        slow.next = None

        # reverse second half
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # combine the two
        dummy = ans = ListNode()
        l1 = head
        l2 = prev
        flag = True 
        while l1 and l2: 
            if flag: 
                ans.next = l1
                ans = ans.next
                l1 = l1.next
                flag = False
            else:
                ans.next = l2
                ans = ans.next
                l2 = l2.next
                flag = True
        if l1: 
            ans.next = l1
        else: 
            ans.next = l2
        


        

