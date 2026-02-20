#
# @lc app=leetcode id=1244 lang=python3
#
# [1244] Design A Leaderboard
#

# @lc code=start
from sortedcontainers import SortedDict
class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.sortedScores = SortedDict()
    
    #O(logN) 
    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else:
            prev = self.scores[playerId]
            num_prev = self.sortedScores[-prev]

            if num_prev == 1:
                del self.sortedScores[-prev]
            else:
                self.sortedScores[-prev] = num_prev - 1
        
            self.scores[playerId] += score
            new_score = prev + score
            self.sortedScores[-new_score] = self.sortedScores.get(-new_score, 0) + 1

    #O(K)
    def top(self, K: int) -> int:
        count, total = 0, 0
        for score, feq in self.sortedScores.items():
            nums_k = self.sortedScores.get(score)
            for _ in range(nums_k):
                total += -score
                count += 1
                if count == K:
                    break
            if count == K:
                break
        return total

    #O(logN)
    def reset(self, playerId: int) -> None:
        prev = self.scores[playerId]
        num_prev = self.sortedScores[-prev]
        if num_prev == 1:
            del self.sortedScores[-prev]
        else:
            self.sortedScores[-prev] = num_prev - 1
        del self.scores[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
# @lc code=end

