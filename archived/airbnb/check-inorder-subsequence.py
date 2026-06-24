import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from templates.tree_node_for_testing import TreeNode, build_tree, tree_to_list

class Solution:
    def is_subsequence(self, root: TreeNode, target: list[int])-> bool:
        idx = 0
        stack = []
        curr = root
        
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if curr.val == target[idx]:
                    idx += 1
                    if idx == len(target):
                        return True
                curr = curr.right
        return False

    def min_operations(self, root, target):
        nodes = []
        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        inorder(root)

        n, m = len(nodes), len(target)
        # longest common subsequence
        dp = [[0] * (m + 1) for _ in range(n + 1)] 
        # (n + 1) * (m + 1): padding at row 0 and col 0
        #dp[i][j]: lens of LCS for nodes[0: i-1] and target[0: m]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if nodes[i-1].val == target[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        min_ops = m - dp[n][m]

        # backtrack through the dp table to find matched elements
        i, j = n, m
        matched = set()
        while i > 0 and j > 0:
            if nodes[i-1].val == target[j-1]:
                matched.add(j-1)
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]: # move up, skip an ele in nodes
                i -= 1
            else: # move left, skip an ele in target
                j -= 1
        
        edits = []
        for j in range(m):
            if j not in matched:
                edits.append(f"Insert {target[j]}")
            else:
                edits.append(f"Keep {target[j]}")
        return min_ops, edits


s = Solution()

input_values = [2, 1, 4, None, None, None, 5]
target = [1, 4]
root = build_tree(input_values)
print(s.is_subsequence(root, target))

ops, edits = s.min_operations(root, [1, 4, 6])
print(ops)
print(edits)