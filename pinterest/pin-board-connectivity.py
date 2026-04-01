from typing import List, Optional

class UnionFind:
    def __init__(self):
        self.parent = {} # 1. parent. dict based union find
        self.height = {} # 2. Rank: Height of the tree (for balancing)
        
    def find(self, x: int) -> int:
        if x not in self.parent:
            self.parent[x] = x
            self.height[x] = 0
            return x
        
        if self.parent[x] == x:
            return x
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
        return True 

class Solution:
    def areRelated(self, boards: List[List[int]], pin1: int, pin2: int) -> bool:
        # TODO: Implement areRelated logic
        uf = UnionFind()
        for board in boards:
            if not board:
                continue
            first_pin = board[0]
            for i in range(1, len(board)):
                uf.union(first_pin, board[i])
            
        # If the roots of both pins are the same, they are related
        return uf.find(pin1) == uf.find(pin2)
        # $O(B * alpha(U)),

from collections import deque, defaultdict
# BFS solution
def are_pins_related_bfs(boards, pin1, pin2):
    # Quick check: if pins are the same, they are related
    if pin1 == pin2:
        return True
        
    # 1. Build the Graph
    # adjacency list: {pin: set of neighbor_pins}
    graph = defaultdict(set)
    for board in boards:
        for i in range(len(board)):
            for j in range(i + 1, len(board)):
                u, v = board[i], board[j]
                graph[u].add(v)
                graph[v].add(u)
                
    # If the starting pin isn't in our graph, it can't reach anything
    if pin1 not in graph:
        return False

    # 2. Standard BFS
    queue = deque([pin1])
    visited = {pin1}
    
    while queue:
        current_pin = queue.popleft()
        
        if current_pin == pin2:
            return True
            
        for neighbor in graph[current_pin]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return False