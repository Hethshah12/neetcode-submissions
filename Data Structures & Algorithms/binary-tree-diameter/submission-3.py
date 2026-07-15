# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_d=[0]

        def height(root):
            if root is None:
                return 0
            left_h=height(root.left)
            right_h=height(root.right)
            diameter=left_h + right_h
            largest_d[0]=max(largest_d[0], diameter)
            return 1+max(left_h, right_h)
        height(root)
        return largest_d[0]

        # largest_d=0

        # def height(root):
        #     nonlocal largest_d
        #     if not root:
        #         return 0
            
        #     le=height(root.left)
        #     ri=height(root.right)
        #     diam=le+ri
        #     largest_d=max(largest_d, diam)

        #     return 1+ max(le, ri)
        # height(root)
        # return largest_d