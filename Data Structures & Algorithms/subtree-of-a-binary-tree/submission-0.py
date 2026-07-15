# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            if not p and not q:
                return True
            if (not p and q) or (p and not q):
                return False
            if p.val!=q.val:
                return False
            
            #if all of them pass then go to left and then right and check for the same 
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        
        def isitsubtree(root):
            if not root:
                return False
            
            if sameTree(root, subRoot):
                return True

            return isitsubtree(root.left) or isitsubtree(root.right)
        return isitsubtree(root)
