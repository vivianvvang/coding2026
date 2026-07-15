from collections import defaultdict, deque

def isValidForest(edges):
    if not edges:
        return True

    graph = defaultdict(list)
    indegree = defaultdict(int)
    nodes = set()

    for u, v in edges:
        if u == v:
            return False

        
        graph[u].append(v)
        indegree[v] += 1
        if indegree[v] > 1:
            return False
        indegree[u] += 0

        nodes.add(u)
        nodes.add(v)

    q = deque()

    for node in nodes:
        if indegree[node] == 0:
            q.append(node)
    
    visited_cnt = 0
    while q:
        node = q.popleft()
        visited_cnt += 1
        for child in graph[node]:
            indegree[child] -= 1

            if indegree[child] == 0:
                q.append(child)
    return visited_cnt == len(nodes)


def test_is_valid_forest():
    assert isValidForest([]) is True

    assert isValidForest([
        (1, 2),
        (1, 3),
        (2, 4),
    ]) is True

    assert isValidForest([
        (1, 2),
        (3, 4),
        (5, 6),
    ]) is True

    assert isValidForest([
        (1, 3),
        (2, 3),
    ]) is False

    assert isValidForest([
        (1, 2),
        (2, 3),
        (3, 1),
    ]) is False

    assert isValidForest([
        (1, 1),
    ]) is False

    assert isValidForest([
        (1, 2),
        (1, 2),
    ]) is False

    assert isValidForest([
        (1, 2),
        (2, 3),
        (1, 3),
    ]) is False

    print("All tests passed!")


test_is_valid_forest()