# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        while curr: 
            if curr.val == 9999:
                return True
            else: 
                curr.val = 9999
            curr = curr.next
        return False