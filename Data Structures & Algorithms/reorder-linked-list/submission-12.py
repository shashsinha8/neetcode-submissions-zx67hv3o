# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head: 
            return None
        if head.next is None: 
            return

        # find mid
        slow, fast = head, head 
        end = None
        while fast and fast.next: 
           end = slow
           slow = slow.next
           fast = fast.next.next

        # print(end.val, slow.val)
        # split halves (handle end of first list)
        end.next = None
        
        # reverse second half 
        prev = None
        while slow: 
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # curr = prev
        # while curr: 
        #     print(curr.val, end="->")
        #     curr = curr.next


        # merge two lists

        curr = dummy = ListNode()
        flag = True
        front = head
        while front and prev: 
            if flag: 
                curr.next = front
                front = front.next
                curr = curr.next
                flag = False
            else: 
                curr.next = prev
                prev = prev.next
                curr = curr.next
                flag = True
        
        if front: curr.next = front
        else: curr.next = prev

               
