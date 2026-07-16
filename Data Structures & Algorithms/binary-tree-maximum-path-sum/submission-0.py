# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res=[root.val]

        #return the max path sum without splitting 
        def dfs(root):
            if not root:
                return 0
            
            leftm=dfs(root.left)
            rightm=dfs(root.right)

            leftm, rightm = max(leftm,0), max(rightm, 0)
#the max sum with the split will be stored in result 
            res[0]= max(res[0], root.val + leftm+rightm)
#return value will be without splitting ofc 
            return root.val+max(leftm, rightm)

        dfs(root)
        return res.pop()