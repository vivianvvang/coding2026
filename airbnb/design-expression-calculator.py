import collections
from typing import List

class Spreadsheet:
    def __init__(self):
        # Stores the current, fully evaluated integer value for O(1) retrieval
        self.val_dict = {} 
        # Maps a key to its list of dependencies: "C" -> ["A", "B"]
        self.formulas = {} 
        
        # Adjacency list for the reverse graph: "A" -> {"C", "D"}
        # This tells us which nodes need to be updated when a key changes
        self.dependents = collections.defaultdict(set)

    def _remove_old_dependencies(self, key: str):
        """Helper to clean up the graph when a key's formula is overwritten."""
        if key in self.formulas:
            for dep in self.formulas[key]:
                self.dependents[dep].discard(key)
            del self.formulas[key]

    def _update(self, start_key: str):
        """Updates all downstream nodes in Topological Order."""
        # 1. BFS to find all reachable downstream nodes in dependents graph
        reachable = {start_key}
        q = collections.deque([start_key])
        
        while q:
            curr = q.popleft()
            for child in self.dependents[curr]:
                if child not in reachable:
                    reachable.add(child)
                    q.append(child)
        
        # 2. Calculate in-degrees for the induced subgraph based on depaendents
        in_degree = collections.defaultdict(int)
        for node in reachable:
            for child in self.dependents[node]:
                if child in reachable:
                    in_degree[child] += 1
                    
        # 3. Topological Sort to recalculate values safely
        topo_q = collections.deque([start_key])
        
        while topo_q:
            curr = topo_q.popleft()
            
            # Recalculate if it's a formula (skip if it was just a literal value update)
            if curr in self.formulas:
                self.val_dict[curr] = sum(self.val_dict.get(dependent, 0) for dependent in self.formulas[curr])
                
            for child in self.dependents[curr]:
                if child in reachable:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        topo_q.append(child)
            # all vals are updated

    def set_value(self, key: str, value: int):
        # Optimization: If the value is identical and it's not overwriting a formula, do nothing
        if key not in self.formulas and self.val_dict.get(key) == value:
            return

        self._remove_old_dependencies(key)
        self.val_dict[key] = value
        
        # Trigger updates for anything that depends on this key
        self._update(key)

    def set_sum(self, key: str, values: List[str]):
        self._remove_old_dependencies(key)
        
        # Set the new formula
        self.formulas[key] = values
        for v in values:
            self.dependents[v].add(key)
            
        # Trigger updates. Since 'key' is now a formula, _update 
        # will evaluate it first, then cascade to its dependents.
        self._update(key)

    def get_value(self, key: str) -> int:
        # Optimized to O(1), optimal solution for read heavy system
        return self.val_dict.get(key, 0)