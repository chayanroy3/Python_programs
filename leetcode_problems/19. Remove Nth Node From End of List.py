# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next==None:
            return None
        else:
            i,j=head,head
            for k in range(0,n):
                j=j.next
            if j is None:
                return head.next
            while j.next is not None:
                j=j.next
                i=i.next
            i.next=i.next.next
            return head
