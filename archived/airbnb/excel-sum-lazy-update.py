from collections import defaultdict, Counter, deque

class LazyReactiveSolution:
    def __init__(self):
        self.values = defaultdict(int)
        self.formulas = defaultdict(dict)
        self.dependents = defaultdict(set)
        
        # A set keeping track of variables that need to be recalculated
        self.is_dirty = set()

    def _clear_old_dependencies(self, key: str) -> None:
        for d in self.formulas[key].keys():
            self.dependents[d].discard(key)
        self.formulas[key] = {}

    def _mark_dirty(self, start_key: str) -> None:
        """
        Fast invalidation: Spreads the dirty flag downstream. 
        If a node is already dirty, we don't need to visit its dependents
        because they must already be dirty too! This saves massive compute time.
        """
        q = deque([start_key])
        while q:
            curr = q.popleft()
            for nxt in self.dependents[curr]:
                if nxt not in self.is_dirty:
                    self.is_dirty.add(nxt)
                    q.append(nxt)

    def set_value(self, key: str, value: int) -> None:
        self._clear_old_dependencies(key)
        self.values[key] = value
        
        self.is_dirty.discard(key)
        # Mark everything downstream as dirty
        self._mark_dirty(key)

    def set_sum(self, key: str, dependencies: list) -> None:
        self._clear_old_dependencies(key)
        
        formula_dict = dict(Counter(dependencies))
        self.formulas[key] = formula_dict
        for d in formula_dict.keys():
            self.dependents[d].add(key)
            
        # Don't calculate the math here! Just mark it as dirty.
        self.is_dirty.add(key)
        self._mark_dirty(key)

    def get_value(self, key: str) -> int:

        if key not in self.is_dirty:
            return self.values.get(key, 0)

        total = 0
        for dep, count in self.formulas[key].items():
            total += self.get_value(dep) * count
            
        self.values[key] = total
        
        self.is_dirty.remove(key)
        
        return total


# --- Quick Verification ---
r = LazyReactiveSolution()
r.set_value("A", 5)
r.set_value("B", 10)
r.set_sum("C", ["A", "B"])
r.set_sum("D", ["C", "C", "A"])

print(f"Read D: {r.get_value('D')}") # Evaluates C and D on demand. Returns 35.
r.set_value("A", 100) # Instantly marks C and D as dirty. No math is done.
print(f"Read D again: {r.get_value('D')}") # Re-evaluates C and D. Returns 320.