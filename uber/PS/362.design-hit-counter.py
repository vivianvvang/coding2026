#
# @lc app=leetcode id=362 lang=python3
#
# [362] Design Hit Counter
#

# @lc code=start
class HitCounter:

    def __init__(self):
        self.window = 300
        self.times = [0] * 300
        self.hits = [0] * 300

    def hit(self, timestamp: int) -> None:
        idx = timestamp % self.window
        if self.times[idx] == timestamp:
            self.hits[idx] += 1
        else:
            self.times[idx] = timestamp
            self.hits[idx] = 1

    def getHits(self, timestamp: int) -> int:
        ans = 0 
        for i in range(self.window):
            if self.times[i] > timestamp - 300:
                ans += self.hits[i]
        return ans
        
"""
Million Input:
- Batching: Instead of calling GlobalCounter.hit() 1,000 times, the thread increments its private local_count. Once the buffer reaches a threshold (e.g., 1,000 hits) or a time limit (e.g., 100ms), it performs one single "bulk update" to the global counter: GlobalCounter.add(1000). It reduces the number of times the CPU has to synchronize memory across cores
lose Real-time Accuracy.
- Sharding: Instead of one giant counter, we split it into $N$ independent counters (shards).
When a "hit" comes in, we assign it to a shard using a hash function (like ThreadID % N or Hash(UserID) % N).
hit() remains $O(1)$, but getHits() becomes NumOfShard * 300

"""

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
# @lc code=end

