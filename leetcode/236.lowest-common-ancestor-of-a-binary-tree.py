#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = None

        def helper(root):
            nonlocal lca
            if root is None:
                return 0
            find = 0
            if root == p or root == q:
                find = 1
            
            left = helper(root.left)
            right = helper(root.right)
            if left + right + find == 2:
                lca = root
            return 1 if (find + left + right) >= 1 else 0

        helper(root)
        return lca
# @lc code=end

