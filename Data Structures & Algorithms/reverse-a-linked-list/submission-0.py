# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values=[]
        curr =head
        while curr :
            values.append(curr.val)
            curr=curr.next
        dummy=ListNode(-1)
        curr=dummy
        

        for i in values[::-1]:
            temp=ListNode(i)
            curr.next=temp
            curr=temp
        return dummy.next


        