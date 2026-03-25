from typing import List, Optional
from collections import deque, defaultdict
class DetectionSystem:
    def __init__(self, threshold: int, windowSize: int):
        self.threshold = threshold
        self.windowSize = windowSize
        self.map = defaultdict(deque)

    def isBot(self, timestamp: int, ip: str) -> bool:
        requests = self.map[ip]
        windowStart = timestamp - self.windowSize + 1
        while requests and requests[0] < windowStart:
            requests.popleft()
        requests.append(timestamp)
        return len(requests) > self.threshold
