# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

#I do a BFS and keep track of the sum of leaves on each level
#The last sum will be the sum of the deepest leaves

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q=deque([root])

        while q:
            level_size=len(q)
            current_sum=0
            for i in range(level_size):
                node=q.popleft()
                current_sum+=node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return current_sum

    
            





       