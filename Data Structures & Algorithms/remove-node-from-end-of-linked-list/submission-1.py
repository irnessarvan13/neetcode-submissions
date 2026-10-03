# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)        # create a dummy node to sit before the real list
        dummy.next = head           # connect dummy to the real list so right can traverse it

        left = dummy                # left starts at dummy, always sits just before the node to remove
        right = dummy               # right starts at dummy, will move n steps ahead of left

        for i in range(n):          # move right forward n steps first
            right = right.next      # right moves forward one step each iteration
                                    # after this loop, right is n steps ahead of left

        while right and right.next: # keep moving until right hits the last node
            left = left.next        # left moves forward one step
            right = right.next      # right moves forward one step
                                    # when loop ends, left is just before the node to remove

        left.next = left.next.next  # skip over the target node
                            # left.next is the node to remove
                            # left.next.next is the node after it

        return dummy.next           # skip the dummy node and return the real list
