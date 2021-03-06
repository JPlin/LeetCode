# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        p = root
        res = []
        stack = []

        while stack or p:
            while p:
                stack.append(p)
                p = p.left

            p = stack.pop()
            res.append(p.val)
            p = p.right
        
        return res

