# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pq = []

        def traverse(root: Optional[TreeNode], heap: list): 
            if root is None:
                return
            traverse(root.right, pq)
            heapq.heappush(pq, -1 * root.val)
            if len(pq) > k:
                heapq.heappop(pq)
            traverse(root.left, pq)
        
        traverse(root, pq)
        return -1 * pq[0]


        