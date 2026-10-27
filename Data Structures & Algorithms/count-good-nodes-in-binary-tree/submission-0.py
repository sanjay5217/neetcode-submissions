# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        
        def get_count(root: TreeNode, max_val: int):
            if not root:
                return 

            val = max_val
            if root.val >= val:
                res[0] += 1
                val = root.val
            get_count(root.right, val)
            get_count(root.left, val)
        
        get_count(root, float("-inf"))
        return res[0]

# res = 2