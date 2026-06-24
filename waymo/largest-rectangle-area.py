def largestRect(points):
    points_set = set([(x, y) for x, y in points])
    res = float('-inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]
            if x1 == x2 or y1 == y2:
                continue
            if (x1, y2) in points_set and (x2, y1) in points_set:
                res = max(res, abs(x1 - x2) * abs(y1 - y2))
    return res if res > float('-inf') else 0        
        
print(largestRect([[0,0],[1,1],[1,0],[0,1],[0,2],[1,2]]))