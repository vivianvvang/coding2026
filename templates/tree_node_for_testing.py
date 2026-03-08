class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return f"TreeNode({self.val})"
    
from collections import deque
from typing import List, Optional

def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    根据层序遍历的数组构建二叉树。
    例如输入: [1, 2, 3, None, None, 4, 5]
    """
    if not values:
        return None
        
    root = TreeNode(values[0])
    queue = deque([root])
    
    i = 1
    
    while queue and i < len(values):
        current = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
        
    return root


def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    将树重新转换为层序遍历的数组，方便对比输出结果。
    """
    if not root:
        return []
        
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
            
    # 去除末尾多余的 None (LeetCode 的标准格式)
    while result and result[-1] is None:
        result.pop()
        
    return result
