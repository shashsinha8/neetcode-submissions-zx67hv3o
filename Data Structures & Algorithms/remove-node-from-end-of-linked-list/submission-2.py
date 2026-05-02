# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        l = dummy = ListNode()
        l.next = head
        r = head
        
        for _ in range(n): 
            r = r.next
        while r:
            l = l.next
            r = r.next
    
        if l and l.next:
            temp = l.next
            l.next = temp.next
            del temp
        elif l and not l.next:
            del l.next
            l.next = None
        return dummy.next

        
        

        


