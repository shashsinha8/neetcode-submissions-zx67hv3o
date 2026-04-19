# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        curr = head
        d = deque()

        while curr:
            d.append(curr)
            curr = curr.next

        curr = d.popleft()

        while d: 
            back = d.pop()
            curr.next = back
            curr = back
            if d: 
                front = d.popleft()
                curr.next = front
                curr = front
        
        curr.next = None
        

        

        


            
            





        

        
