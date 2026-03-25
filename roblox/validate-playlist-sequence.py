from typing import List, Optional

class Solution:
    def isPossibleShuffle(self, allSongs: List[str], playlist: List[str]) -> bool:
        all_songs_set = set(allSongs)

        for song in playlist:
            if len(all_songs_set) == 0:
                all_songs_set = set(allSongs)
            if song in all_songs_set:
                all_songs_set.discard(song)
            else:
                return False
        return True

