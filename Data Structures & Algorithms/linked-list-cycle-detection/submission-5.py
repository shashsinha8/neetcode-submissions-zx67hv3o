# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head


        '''
        slow = 1 
        fast = 1
        ''' 
        while slow: 
            print(f'slow = {slow.val} | fast = {fast.val}')
            if not fast.next or not fast.next.next: 
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False
            
        