from collections import defaultdict, deque
class Counter:
    def __init__(self, window):
        self.window = window
        self.dt = defaultdict(deque)
    
    def put(self, time, ele):
        self.dt[ele].append(time)
        # Calculate the earliest valid timestamp (the cutoff boundary)
        start = time - self.window if time - self.window >= 0 else 0
        # Remove all expired timestamps from the left
        while self.dt[ele] and self.dt[ele][0] < start:
            self.dt[ele].popleft()

    def get_count(self, time, ele):
        start = time - self.window if time - self.window >= 0 else 0
        while self.dt[ele] and self.dt[ele][0] < start:
            self.dt[ele].popleft()
        return len(self.dt[ele])

    def get_total_count(self, time):
        res = 0
        for ele in self.dt.keys():
            res += self.get_count(time, ele)

        return res
    

counter = Counter(10)
counter.put(1, 'a')
counter.put(3, 'a')
counter.put(5, 'b')
print(counter.get_count(6, 'a'))
print(counter.get_total_count(6))
print(counter.get_count(12, 'a'))
print(counter.get_total_count(12))
