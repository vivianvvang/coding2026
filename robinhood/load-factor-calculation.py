from typing import List, Optional
from collections import defaultdict, deque

def loadFactorCalc(serviceList: List[str], entryPoint: str) -> List[str]:
    graph = defaultdict(list)
    load = defaultdict(int)
    defined = set()


    for sl in serviceList:
        service, dependencies = sl.split("=")
        defined.add(service)

    for sl in serviceList:
        service, dependencies = sl.split("=")
        d_list = dependencies.split(",")
        for d in d_list:
            if d in defined:
                graph[service].append(d)
    
    load[entryPoint] = 1
    #1. find reachable services from entry point
    reachable = set()
    queue = deque([entryPoint])
    while queue:
        service = queue.popleft()
        if service in reachable:
            continue
        reachable.add(service)
        for dep in graph[service]:
            queue.append(dep)
    
    #2. compute indegrees
    indegree = {node: 0 for node in reachable}
    for node in reachable:
        for dep in graph[node]:
            if dep in reachable:
                indegree[dep] += 1

    queue = deque()
    for service in reachable:
        if indegree[service] == 0:
            queue.append(service)

    while queue:
        service = queue.popleft()
        for dep in graph[service]:
            if dep in reachable:
                load[dep] += load[service]
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    queue.append(dep)
    result = []
    for service in sorted(reachable):
        result.append(f"{service}*{load[service]}")
    return result

serviceList = ["logging=", "user=logging", "orders=user,foobar", "recommendations=user,orders", "dashboard=user,orders,recommendations"]
entryPoint = "dashboard"
print(loadFactorCalc(serviceList, entryPoint))