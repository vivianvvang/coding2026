#
# @lc app=leetcode id=1244 lang=python3
#
# [1244] Design A Leaderboard
#
import heapq
# @lc code=start
class Leaderboard:

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        # Simply update the dictionary with the new score for the player.
        if playerId in self.scores.keys():
            self.scores[playerId] += score
        else:
            self.scores[playerId] = score

    # Heap for top-K
    # O(K) + O(NlogK) = O(NlogK)
    def top(self, K: int) -> int:
        heap = []
        for x in self.scores.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)
        res = 0
        while heap:
            res += heapq.heappop(heap)
        return res

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0
        
# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
# @lc code=end

