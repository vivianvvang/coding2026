from typing import List, Optional

# versioned state approach
# record only the changes for each relationship.
class SocialNetwork:
    def __init__(self, ):
        # TODO: Initialize SocialNetwork
        self.snaps = {}
        self.relations = {}
        self.snapId = 0

    def follow(self, followerId: int, followeeId: int) -> None:
        self._record_change(followerId, followeeId, True)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self._record_change(followerId, followeeId, False)

    def createSnapshot(self, ) -> int:
        snapId = self.snapId
        self.snapId = self.snapId + 1
        return snapId

    def isFollowing(self, followerId: int, followeeId: int, snapId: int) -> bool:
        key = (followerId, followeeId)
        if key not in self.relations:
            return False
        snap_history = self.snaps[key]

        l, r = 0, len(snap_history)
        while l < r:
            mid = l + (r - l) // 2
            if snap_history[mid] > snapId:
                r = mid
            else:
                l = mid + 1
        found = l - 1
        if found == -1:
            return False
        return self.relations[key][found]
    
    def _record_change(self, followerId, followeeId, isFollowing):
        key = (followerId, followeeId)
        if key not in self.relations:
            self.snaps[key] = []
            self.relations[key] = []
        snap = self.snaps[key]
        relation = self.relations[key]

        if snap and snap[-1] == self.snapId:
            relation[-1] = isFollowing
        else:
            snap.append(self.snapId)
            relation.append(isFollowing)

        
