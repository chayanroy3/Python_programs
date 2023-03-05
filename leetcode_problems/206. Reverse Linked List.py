# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p= head
        if not head:
            return head
        q=p.next
        while q:
            p.next=q.next
            q.next= head
            head = q
            q= p.next
        return head
