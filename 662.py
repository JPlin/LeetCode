# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans , q = 0 , [(root , 1)] # q serve as queue (node , index_num)
        while q:
            new_q , level_min , level_max = [], q[0][1] , q[-1][1]
            ans = max(level_max - level_min + 1 , ans)
            for node , idx in q:
                if node.left: new_q.append((node.left , idx * 2))
                if node.right: new_q.append((node.right , idx * 2 + 1))
            q = new_q
        return ans
