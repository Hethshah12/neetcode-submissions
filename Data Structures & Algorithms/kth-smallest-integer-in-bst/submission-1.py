# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # sorted_arr=[]
        # def sort_tree(root):
        #     if not root:
        #         return None
            
        #     sort_tree(root.left)
        #     sorted_arr.append(root.val)
        #     sort_tree(root.right)

        # sort_tree(root)
        # return sorted_arr[k-1]

        #kind of a better method we do not need to store whole sorted arr

        count=[k]
        res=[0]

        def dfs(root):
            if not root:
                return None
            

            dfs(root.left)
            if count[0]==1:
                res[0]=root.val
            
            count[0]=count[0]-1

            #now we go right only if the value of count is greater than 0 otherwise we would have appended
            if count[0] >0:
                dfs(root.right)
        
        dfs(root)

        return res[0]