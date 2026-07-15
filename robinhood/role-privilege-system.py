from collections import defaultdict, deque

def resolvePrivileges(n, grants, allowedList, disallowedList):
    graph = defaultdict(list)
    indegree = [0] * n
    for parent, child in grants:
        graph[parent].append(child)
        indegree[child] += 1

    allowed = [set(allowed) for allowed in allowedList]
    disallowed = [set(disallowed) for disallowed in disallowedList]

    queue = deque()
    for role in range(n):
        if indegree[role] == 0:
            queue.append(role)
    while queue:
        role = queue.popleft()
        for child in graph[role]:
            allowed[child].update(allowed[role])
            disallowed[child].update(disallowed[role])

            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)
    res = []
    for role in range(n):
        ans = allowed[role] - disallowed[role]
        res.append(sorted(ans))

    return res

n = 3
grants = [[0, 1], [1, 2]]
allowedList = [["B"], ["A"], []]
disallowedList = [[], [], ["B"]]
print(resolvePrivileges(n, grants, allowedList, disallowedList)) 


n = 3
grants = [[0, 1], [0, 2]]
allowedList = [["B"], ["A"], []]
disallowedList = [[], [], ["B"]]
print(resolvePrivileges(n, grants, allowedList, disallowedList)) 


n = 4
grants = [[0, 1], [1, 2], [1, 3]]
allowedList = [["A", "B"], ["C"], ["D"], ["E"]]
disallowedList = [[], ["B"], [], ["A"]]
print(resolvePrivileges(n, grants, allowedList, disallowedList)) 
