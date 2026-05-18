# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head or not head.next: 
            return None

        dummy = ListNode(0, head)
        curr = head
        for i in range(n):
            curr = curr.next

        lag = dummy
        while curr:
            lag = lag.next
            curr = curr.next

        if lag and lag.next: 
            lag.next = lag.next.next

        return dummy.next