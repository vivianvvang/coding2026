#
# @lc app=leetcode id=1101 lang=python3
#
# [1101] The Earliest Moment When Everyone Become Friends
#

# @lc code=start
from typing import List
from collections import defaultdict, deque

class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.height = [1] * n # 2. Rank: Height of the tree (for balancing)
        self.count = n # Optional: Track count of components
        
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False # already connected
        
        # union by height: attach smaller tree to larger tree
        if self.height[root_x] > self.height[root_y]:
            self.parent[root_y] = root_x
        elif self.height[root_x] < self.height[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.height[root_x] += 1
        self.count += 1
        return True 
        
class Solution:

    
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        uf = UnionFind(n)
        group_cnt = n
        for timestamp, a, b in logs:
            if uf.union(a, b):
                group_cnt -= 1
            if group_cnt == 1:
                return timestamp
        return -1
        
# @lc code=end
class RideSystem:
    def __init__(self, n):
        self.n = n
        self.adj = defaultdict(list)    # 连通图
        self.blocks = defaultdict(set)  # 屏蔽列表
        self.num_components = n         # 初始时每个人都是孤岛

    def add_block(self, u, v):
        """记录 u 和 v 互相拉黑"""
        self.blocks[u].add(v)
        self.blocks[v].add(u)

    def process_ride(self, timestamp, u, v):
        """
        尝试让 u 和 v 拼车。
        返回: True (成功合并), False (因屏蔽无法合并或已经合并)
        """
        # 1. 如果已经连通，直接返回
        if self.is_connected(u, v):
            return True

        # 2. 找到 u 和 v 所在的整个群体 (Component)
        component_u = self.get_component(u)
        component_v = self.get_component(v)

        # 3. 核心：检查两个群体之间是否有 Block 关系
        # 只要 Group U 里的任何人屏蔽了 Group V 里的任何人，就不能合并
        if self.has_conflict(component_u, component_v):
            print(f"Time {timestamp}: Merge conflict between group {u} and group {v}")
            return False
        
        # 4. 没有冲突，添加边，物理合并
        self.adj[u].append(v)
        self.adj[v].append(u)
        self.num_components -= 1
        
        # 检查是否所有人连通
        if self.num_components == 1 and self.get_component_size(u) == self.n:
            print(f"Time {timestamp}: Everyone is connected!")
            return True
            
        return True

    def get_component(self, start_node):
        """用 BFS 获取整个连通分量的所有节点"""
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        
        members = []
        while queue:
            node = queue.popleft()
            members.append(node)
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return members

    def is_connected(self, u, v):
        """BFS 检查两点是否已连通"""
        if u == v: return True
        visited = set()
        queue = deque([u])
        visited.add(u)
        while queue:
            node = queue.popleft()
            if node == v: return True
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return False

    def has_conflict(self, group_a, group_b):
        """
        检查两个群体是否有敌对关系
        优化：遍历较小的那个群体的 Block List
        """
        # 为了效率，我们可以遍历 group_a 中的每个人，看他的 block list 是否与 group_b 有交集
        # 优化点：将 group_b 转为 set 以实现 O(1) 查找
        set_b = set(group_b)
        
        for member_a in group_a:
            # 检查 member_a 屏蔽的人里，有没有在 group_b 里的
            # 利用集合求交集：blocks[member_a] AND set_b
            if not self.blocks[member_a].isdisjoint(set_b):
                return True
        return False
