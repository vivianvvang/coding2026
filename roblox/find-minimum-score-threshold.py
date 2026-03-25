from typing import List, Optional
from collections import defaultdict
class Solution:
    def findMinScore(self, games: List[List[str]], threshold: float) -> int:
        n, n_loses = len(games), 0
        stats = defaultdict(lambda: [0, 0]) # score -> num_games==score, num_lost_game_with_score

        for s, result in games:
            score = int(s)
            stats[score][0] += 1
            if result == "lose":
                stats[score][1] += 1
                n_loses += 1
        
        if n > 0 and (n_loses / n) >= threshold:
            return 0
        
        for score in sorted(stats.keys()):
            games_at_score, loses_at_score = stats[score]
            n -= games_at_score
            n_loses -= loses_at_score

            if n == 0:
                break
 
            if n_loses / n >= threshold:
                return score + 1
        return -1


