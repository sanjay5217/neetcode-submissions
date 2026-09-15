# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
    
        main = []
        queue = [root]
        
        while queue:
            temp1 = []
            temp_m = []
            for node in queue:
                temp1.append(node.val)
                if node.left:
                    temp_m.append(node.left)
                if node.right:
                    temp_m.append(node.right)
            main.append(temp1)
            queue = temp_m
        
        return main

