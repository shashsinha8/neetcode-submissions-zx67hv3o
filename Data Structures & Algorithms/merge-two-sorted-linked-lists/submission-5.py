# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        '''
        list1=[1,2,4]
        list2=[1,3,5]
        '''
        dummy = ListNode()
        tail = dummy

        curr1, curr2 = list1, list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
            
        if curr2:
            tail.next = curr2
        elif curr1:
            tail.next = curr1
        
        return dummy.next