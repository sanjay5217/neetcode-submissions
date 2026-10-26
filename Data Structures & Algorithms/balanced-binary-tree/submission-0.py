# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True         
        
        def get_height(root: Optional[TreeNode]) -> int:
            if not root: 
                return 0
            if not root.left and not root.right:
                return 1
            
            return max(get_height(root.left), get_height(root.right)) + 1

        return self.isBalanced(root.left) and self.isBalanced(root.right) and \
                abs(get_height(root.left) - get_height(root.right)) <= 1