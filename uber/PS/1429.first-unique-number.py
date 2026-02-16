from collections import deque, Counter

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque(nums)
        self.counter = Counter(nums)

    def showFirstUnique(self) -> int:
        while self.q:
            if self.counter[self.q[0]] == 1:
                return self.q[0]
            else:
                self.q.popleft()
        return -1
        

    def add(self, value: int) -> None:
        if self.counter[value] == 0:
            self.q.append(value)
        self.counter[value] += 1