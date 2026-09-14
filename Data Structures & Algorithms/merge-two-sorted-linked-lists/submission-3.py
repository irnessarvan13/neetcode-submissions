# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)        # left side — create a dummy node with value -1 to start the new list
        current = dummy             # left side — current starts at the dummy node, it will build the new list from here

        while list1 and list2:      # keep looping as long as both lists still have nodes
            if list1.val <= list2.val:      # right side — reading both values, asking which one is smaller
                current.next = list1        # left side — attach list1's front node to the new list
                list1 = list1.next          # left side — move list1 forward, its next node is now the front
            else:                           # list2's value is smaller
                current.next = list2        # left side — attach list2's front node to the new list
                list2 = list2.next          # left side — move list2 forward, its next node is now the front
            current = current.next          # left side — move current forward to the newly attached node
                                        # current must always sit at the END of the new list
                                        # so it's ready to attach the next node

        if list1:                   # if list1 still has nodes left after the loop
            current.next = list1    # left side — attach the entire remaining list1 to the end
        if list2:                   # if list2 still has nodes left after the loop
            current.next = list2    # left side — attach the entire remaining list2 to the end

        return dummy.next           # right side — reading dummy.next which is the first real node
                                # skips the dummy -1 node and returns the merged sorted list