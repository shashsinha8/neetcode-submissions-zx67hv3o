# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        curr = head
        l = dummy

        counter = 1
        while curr:
            print(l.val, curr.val)
            if counter > n:
                l = l.next
            curr = curr.next
            counter += 1
        print(l.val)
        
        l.next = l.next.next

        return dummy.next