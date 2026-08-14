# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ls1=[]
        ls2=[]
        while l1 and l2 :
            ls1.append(l1.val)
            ls2.append(l2.val)
            l1=l1.next
            l2=l2.next
        print(ls1)
        res=[ x+y for x,y in zip(ls1,ls2)]
        dummy=ListNode(0)
        curr=dummy
        for i in res:
            if len(str(i))>1:
                tempy=str(i)
                for j in tempy[::-1]:
                    curr.next=ListNode(int(j))
                    curr=curr.next
            else:
                curr.next=ListNode(i)
                curr=curr.next

        return dummy.next


        