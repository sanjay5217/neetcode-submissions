# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        self.mutate_root(root, val)
        return root

    def mutate_root(self, root: Optional[TreeNode], val: int) -> None:
        if root is None:
            root = TreeNode(val)
        elif root.left is None and root.right is None:
            if val < root.val:
                root.left = TreeNode(val)
            else:
                root.right = TreeNode(val)
        elif root.left is None:
            if val < root.val:
                root.left = TreeNode(val)
            else:
                self.mutate_root(root.right, val)
        elif root.right is None:
            if val < root.val:
                self.mutate_root(root.left, val)
            else:
                root.right = TreeNode(val)
        else:
            if val < root.val:
                self.mutate_root(root.left, val)
            else:
                self.mutate_root(root.right, val)


