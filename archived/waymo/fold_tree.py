import sys
import os

# 魔法咒语：获取当前脚本所在目录的上一级目录（也就是根目录），并塞进 Python 的查找路径中
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# 只要在 sys.path.append 之后导入，就不会报错了
from templates.tree_node_for_testing import TreeNode, build_tree, tree_to_list
from typing import Optional
class Solution:
    def fold_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        if root.left is None and root.right is None:
            return root
        root.left = self.fold_tree(root.left)
        root.right = self.fold_tree(root.right)
        if (root.left is None) != (root.right is None):
            child = root.left if root.left is not None else root.right
            root.val += child.val
            root.left = child.left
            root.right = child.right
        print(root, tree_to_list(root))
        return root



input_values = [1, 2, None, 3] 
root = build_tree(input_values)
solution = Solution()
new_root = solution.fold_tree(root)
print(f"res: {tree_to_list(new_root)}")

input_values = [1, 2, None, 3, 4] 
root = build_tree(input_values)
new_root = solution.fold_tree(root)
print(f"res: {tree_to_list(new_root)}")