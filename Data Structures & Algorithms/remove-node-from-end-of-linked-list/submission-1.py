# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = head

        # Move right pointer n steps ahead
        for _ in range(n):
            right = right.next

        # If right is None, we need to remove the head
        if not right:
            return head.next

        # Move both pointers until right reaches the end
        while right.next:
            left = left.next
            right = right.next

        # Remove the nth node from end
        left.next = left.next.next

        return head