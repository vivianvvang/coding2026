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
        if playerId in self.scores.keys():
            self.scores[playerId] += score
        else:
            self.scores[playerId] = score

    # O(K) + O(NlogK)
    def top(self, K: int) -> int:
        min_scores = list(self.scores.values())
        min_scores = [ i * -1 for i in min_scores]
        heapq.heapify(min_scores)
        ans = 0
        for i in range(K):
            ans += -1 * heapq.heappop(min_scores)
        return ans

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0
        
# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
# @lc code=end

