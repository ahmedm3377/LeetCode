# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head

        pointer = head
        head2 = pointer.next
        pointer2 = head2
        while pointer2 and pointer and pointer2.next and pointer.next:
            pointer.next = pointer.next.next
            pointer2.next = pointer2.next.next
            pointer = pointer.next
            pointer2 = pointer2.next



        pointer.next = head2

        return head