class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class BoundaryTraversal:
    def solve_boundary(self, root):
        if not root:
            return []
        
        # 1. 层序遍历收集每一层的首尾节点
        left_nodes = []
        right_nodes = []
        
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                curr = queue.popleft()
                
                # 记录每一层最左边的点
                if i == 0:
                    left_nodes.append(curr.val)
                
                # 记录每一层最右边的点
                # 注意：如果这层只有一个点，i 既是 0 也是 level_size - 1
                if i == level_size - 1:
                    right_nodes.append(curr.val)
                
                for child in curr.children:
                    queue.append(child)
        
        # 2. 拼接路径
        # 题目要求：左下 -> 顶 -> 右下
        
        # 第一部分：左下到顶（left_nodes 的逆序）
        # [L_max, L_max-1, ..., L_1, Root]
        up_path = left_nodes[::-1]
        
        # 第二部分：从顶向下到右下（right_nodes 跳过根节点）
        # [R_1, R_2, ..., R_max]
        down_path = right_nodes[1:]
        
        return up_path + down_path

# --- 测试用例 ---
#      1
#    / | \
#   2  3  4
#  / \    |
# 5   6   7
# 层序结果：
# Level 0: [1] -> left: 1, right: 1
# Level 1: [2, 3, 4] -> left: 2, right: 4
# Level 2: [5, 6, 7] -> left: 5, right: 7

root = Node(1, [
    Node(2, [Node(5), Node(6)]),
    Node(3),
    Node(4, [Node(7)])
])

sol = BoundaryTraversal()
# 预期结果：[5, 2, 1, 4, 7]
print(f"绕行路径: {sol.solve_boundary(root)}")