from typing import List, Optional

class Vector2D:
    def __init__(self, vec2d: List[List[int]]):
        self.vec = vec2d
        self.nr = 0 # next availble r
        self.nc = 0 # next availble c
        self.lr = -1 
        self.lc = -1 

    def next(self, ) -> int:
        if not self.hasNext():
            print("no next ele")
            return -1
        self.lr, self.lc = self.nr, self.nc
        val = self.vec[self.nr][self.nc]
        self.nc += 1
        return val

    def hasNext(self, ) -> bool:
        # move and stop at next availble element
        while self.nr < len(self.vec) and self.nc >= len(self.vec[self.nr]):
            self.nr += 1
            self.nc = 0
        return self.nr < len(self.vec)

    def remove(self, ) -> None:
        if self.lr == -1:
            print("double removing")
            return
        self.vec[self.lr].pop(self.lc)

        # If we removed an element from the row we are currently iterating,
        # we must shift the 'col' pointer back by 1.
        if self.lr == self.nr:
            self.nc -= 1
        self.lr, self.lc = -1, -1 #prevent double removing

    def getVectorSnapshot(self, ) -> List[List[int]]:
        res = []
        for r in self.vec:
            res.append(list(r))
        return res

vec2d = Vector2D([[1,2],[3,4]])
vec2d.hasNext()
vec2d.next()
vec2d.hasNext()
vec2d.next()
vec2d.remove()
vec2d.getVectorSnapshot()
vec2d.hasNext()
vec2d.next()
vec2d.hasNext()
vec2d.next()
vec2d.hasNext()