# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        # Compute the length of the list and get the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Adjust k to be within the bounds of the list length
        k %= length
        if k == 0:
            return head

        # Find the new tail node (k steps from the end)
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # The new head is the node after the new tail
        new_head = new_tail.next
        new_tail.next = None
        tail.next = head

        return new_head