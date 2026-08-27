# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ls=[]
        while list1:
            ls.append(list1.val)
            list1=list1.next
        while list2:
            ls.append(list2.val)
            list2=list2.next
        ls.sort()
        dummy=ListNode(-1)
        curr=dummy
        for i in ls:
            temp=ListNode(i)
            curr.next=temp
            curr=curr.next
        return dummy.next
        