# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        '''
        124
        135

        curr1 = 4 
        curr2 = 3

        ans = Node
        [node, 1, 1, 2, ]
        ans_end = 
        

        '''    


        curr1 = list2
        curr2 = list1

        ans = ListNode()
        ans_end = ans

        while curr1 and curr2: 
            if curr1.val <= curr2.val:
                ans_end.next = ListNode(curr1.val)
                curr1 = curr1.next
            else: 
                ans_end.next = ListNode(curr2.val)
                curr2 = curr2.next
            ans_end = ans_end.next
        
        if curr1:
            ans_end.next = curr1
        else: 
            ans_end.next = curr2
        
        return ans.next

            