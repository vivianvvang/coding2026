from collections import defaultdict, deque
from typing import List

class UnboundMatrix:
    def __init__(self, ):
        self.rows = defaultdict(list)
        self.cols = defaultdict(list)
        self.points = set()

    def addPoint(self, x: int, y: int) -> None:
        point = (x, y)
        if point in self.points:
            return

        self.points.add(point)
        self.rows[x].append(point)
        self.cols[y].append(point)

    def isConnected(self, point1: List[int], point2: List[int]) -> bool:
        return self.getMinSteps(point1, point2) != -1

    def getMinSteps(self, start: List[int], end: List[int]) -> int:
        start = tuple(start)
        end = tuple(end)

        if start not in self.points or end not in self.points:
            return -1

        if start == end:
            return 0

        queue = deque([(start, 0)])
        visited_points = {start}

        visited_rows = set()
        visited_cols = set()

        while queue:
            (row, col), steps = queue.popleft()

            if (row, col) == end:
                return steps

            if row not in visited_rows:
                visited_rows.add(row)

                for next_point in self.rows[row]:
                    if next_point not in visited_points:
                        visited_points.add(next_point)
                        queue.append((next_point, steps + 1))

            if col not in visited_cols:
                visited_cols.add(col)

                for next_point in self.cols[col]:
                    if next_point not in visited_points:
                        visited_points.add(next_point)
                        queue.append((next_point, steps + 1))

        return -1