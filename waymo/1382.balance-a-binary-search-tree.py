#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sorted_nodes= []
        def _inorder_traversal(node):
            if not node:
                return
            _inorder_traversal(node.left)
            sorted_nodes.append(node)
            _inorder_traversal(node.right)
        
        _inorder_traversal(root)

        # divide & conquer
        def _build_balenced(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            current_root = sorted_nodes[mid]

            current_root.left = _build_balenced(left, mid - 1)
            current_root.right = _build_balenced(mid + 1, right)
            return current_root
        
        return _build_balenced(0, len(sorted_nodes) - 1)
            
        
# @lc code=end

