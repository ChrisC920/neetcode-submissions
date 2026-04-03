# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        h = slow.next
        prev = slow.next = None
        while h:
            temp = h.next
            h.next = prev
            prev = h
            h = temp
        l1, l2 = head, prev
        while l1 and l2:
            temp1, temp2 = l1.next, l2.next
            l1.next = l2
            l1 = temp1
            l2.next = l1
            l2 = temp2 
