"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #first of all if there is nothing then return none 
        if not head:
            return None
        
        curr=head
        o_to_n={}

        while curr:
            node= Node(x=curr.val)
            o_to_n[curr]=node
            curr=curr.next
        
        curr=head
        while curr:
            new_node=o_to_n[curr]
            new_node.next=o_to_n[curr.next] if curr.next else None
            new_node.random=o_to_n[curr.random] if curr.random else None

            curr=curr.next
        
        return o_to_n[head]
