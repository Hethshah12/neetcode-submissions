# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sett=set()
        curr=head
        while curr:
            if curr in sett:
                return True
            sett.add(curr)
            curr=curr.next
        return False