# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # def height(root):
        #     if not root:
        #         return True
        #     lh=height(root.left)
        #     rh=height(root.right)
        #     diff=abs(lh-rh) or abs(rh-lh)
        #     if not (diff<=1) :
        #         return False
        #     return True

        # return height(root)

        balanced= True

        def height(root):
            nonlocal balanced
            if not root:
                return 0

            lh=height(root.left)
            if balanced is False: #early stopping 
                return 0
            rh=height(root.right)

            if abs(lh-rh) >1:
                balanced=False
                return 0

            return 1+ max(lh, rh)

        height(root)
        return balanced
