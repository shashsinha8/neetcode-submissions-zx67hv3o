# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if head.next is None: 
            return
        
        slow = fast = head
        temp = None
        # find midpoint
        while fast and fast.next: 
            temp = slow
            slow = slow.next
            fast = fast.next.next
        
        # for odd slow is midpoint else after mid
        # reverse second half

        temp.next = None
        prev = None

        while slow: 

            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
      
        # create dummy and link the two alternately

        dummy = curr = ListNode()
        l1 = head
        l2 = prev

        # head=[2,4,6,8,9]
        # [2,4]
        # [6,8,9]
        flag = True
        while l1 and l2: 
            if flag:
                curr.next = l1
                curr = l1
                l1 = l1.next
                flag = False
            else:
                curr.next = l2
                curr = l2
                l2 = l2.next
                flag = True
            
        if l1: 
            curr.next = l1
        else: 
            curr.next = l2
            
        
        

        


            
            





        

        
