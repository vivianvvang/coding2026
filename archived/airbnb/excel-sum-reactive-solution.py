
from collections import defaultdict, deque, Counter

class ReactiveSolution:
    def __init__(self):
        self.values = defaultdict(int)
        self.formulas = defaultdict(dict)
        self.dependents = defaultdict(set) #val -> elements depend on vals
    
    def _clear_old_dependencies(self, key):
        print("set_clear_old_dependencies_value for key "+ key)
        for d in self.formulas[key].keys():
            self.dependents[d].discard(key)
        self.formulas[key] = {}

    def set_value(self, key: str, value: int):
        print("set_value for key "+ key + " with value " + str(value))
        self._clear_old_dependencies(key)
        self.values[key] = value
        self._update_dependents(key)

    def set_sum(self, key: str, dependencies: list):
        print("set_sum for key "+ key + "with dependencies " + ",".join(dependencies))
        self._clear_old_dependencies(key)
        self.formulas[key] = dict(Counter(dependencies))

        self.values[key] = self._calculate_from_formula(self.formulas[key])
        for d in self.formulas[key].keys():
            self.dependents[d].add(key)
        self._update_dependents(key)
 
    def get_value(self, key: str) -> int:
        print(self.values.get(key, 0))
        return self.values.get(key, 0)
    
    def _calculate_from_formula(self, dependencies):
        sum = 0
        for d, num in dependencies.items():
            sum += self.values.get(d, 0) * num
        print("sum = " + str(sum) + ", calcualted from " + ",".join(dependencies))
        return sum
    
    def _update_dependents(self, key):
        print("updating dependents for " + key) # A's dependents: C & D
        reachable = set() # find all connected nodes of key
        q = deque([key])

        while q:
            curr = q.popleft()
            if curr not in reachable:
                reachable.add(curr)
                for nxt in self.dependents[curr]:
                    q.append(nxt)
        
        # build indegree map for reachable nodes
        indegree = defaultdict(int)
        for node in reachable:
            for dependent in self.dependents[node]:
                if dependent in reachable:
                    indegree[dependent] += 1
        
        topo = deque([key])     
        while(topo):
            curr = topo.popleft()
            if len(self.formulas[curr]) > 0:
                self.values[curr] = self._calculate_from_formula(self.formulas[curr])
            for dependent in self.dependents[curr]:
                if dependent in reachable:
                    indegree[dependent] -= 1
                    if indegree[dependent] == 0:
                        topo.append(dependent)
        return

r = ReactiveSolution()
r.set_value("A", 5)
r.set_value("B", 10)
r.set_sum("C", ["A", "B"])
r.set_sum("D", ["C", "C", "A"])
r.get_value("A")
r.set_value("A", 100) #A changes to 100, triggers updates:
r.get_value("D") #Returns 320


def run_tests():
    print("\n--- Running Tests ---")
    r = ReactiveSolution()

    # Test 1: The Diamond Problem (Your original test case)
    print("\nTest 1: Basic Diamond Problem")
    r.set_value("A", 5)
    r.set_value("B", 10)
    r.set_sum("C", ["A", "B"])         # C = 5 + 10 = 15
    r.set_sum("D", ["C", "C", "A"])    # D = 15 + 15 + 5 = 35
    assert r.get_value("A") == 5
    assert r.get_value("D") == 35
    
    r.set_value("A", 100)              # C = 110, D = 110 + 110 + 100 = 320
    assert r.get_value("D") == 320
    print("Test 1 Passed!")

    # Test 2: Overwriting a Formula with a Raw Value
    print("\nTest 2: Overwrite Formula with Value")
    # Right now D is 320. Let's sever its connection to C and A.
    r.set_value("D", 50)
    assert r.get_value("D") == 50
    # Changing A should NO LONGER affect D, because we cleared old dependencies.
    r.set_value("A", 200) 
    assert r.get_value("D") == 50
    print("Test 2 Passed!")

    # Test 3: Overwriting a Raw Value with a Formula
    print("\nTest 3: Overwrite Value with Formula")
    r.set_value("X", 10)
    r.set_value("Y", 20)
    r.set_sum("A", ["X", "Y"])         # A was previously 200, now it's 10 + 20 = 30
    assert r.get_value("A") == 30
    # Remember, C still depends on A and B. 
    # B is 10. A is now 30. C should have auto-updated to 40.
    assert r.get_value("C") == 40
    print("Test 3 Passed!")

    # Test 4: Default Values (Keys that don't exist yet)
    print("\nTest 4: Default Values")
    # Z has never been set. It should default to 0.
    r.set_sum("E", ["Z", "Z"])         
    assert r.get_value("E") == 0
    # Now if we set Z, E should react.
    r.set_value("Z", 7)
    assert r.get_value("E") == 14
    print("Test 4 Passed!")

    print("\nAll test cases passed successfully! You nailed it.")

# Run the tests
run_tests()