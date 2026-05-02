# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # l = dummy = ListNode(0, head)
        # r = head
        
        # for _ in range(n): 
        #     r = r.next
        # while r:
        #     l = l.next
        #     r = r.next

        # l.next = l.next.next

        # return dummy.next
        dummy = ListNode(0, head)
        curr = head
        length = 0
        while curr: 
            length += 1
            curr = curr.next
        print(length)

        target = length - n
        curr = head
        prev = dummy
        for _ in range(target):
            prev = curr
            curr=curr.next
        print(curr.val)
        prev.next = curr.next
        
        return dummy.next

        
        

        


