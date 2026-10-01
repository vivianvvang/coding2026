def findMiddleCourse(pairs):
    course_map = {}
    prereq_set = set()
    course_set = set()
    for prereq, course in pairs:
        prereq_set.add(prereq)
        course_set.add(course)
        course_map[prereq] = course
    start = (prereq_set - course_set).pop()
    chain = [start]

    while start in prereq_set:
        next = course_map[start]
        chain.append(next)
        start = next
    mid_index = len(chain) // 2
    return chain[mid_index]

pairs = [["Chemistry", "Biology"],["Biology", "ComputerScience"],["Math", "Physics"],["Physics", "Chemistry"]]
print(findMiddleCourse(pairs))

"""
What modifications are needed if the input format switches from edge pairs to an adjacency matrix?
- In an adjacency matrix, indegree is calculated by scanning a column.
"""

from collections import defaultdict, deque
def findLongestPathMiddleCourse(pairs):
        graph = defaultdict(list)
        indegree = defaultdict(int)
        course_set = set()
        
        # Build the graph (adjacency list) and compute in-degrees.
        for prereq, course in pairs:
            graph[prereq].append(course)
            indegree[course] += 1
            indegree[prereq] += 0

            course_set.add(prereq)
            course_set.add(course)
        
        queue = deque()

        longest = {} # dict, course -> longest path len from course
        parent = {} # for path backtracking

        # find all nodes with 0 indegree
        for course in course_set:
            if indegree[course] == 0:
                queue.append(course)
                longest[course] = 1
                parent[course] = None
            else:
                longest[course] = 0
        
        # traverse all paths, update longest
        while queue:
            node = queue.popleft()
            for next in graph[node]:
                temp_lenth = longest[node] + 1
                if temp_lenth > longest[next]:
                    longest[next] = temp_lenth
                    parent[next] = node
                indegree[next] -= 1
                
                if indegree[next] == 0:
                    queue.append(next)
        
        end = max(course_set, key = lambda course: longest[course])

        path = []
        curr = end
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        path.reverse()
        middle_index = (len(path) - 1) // 2
        return path[middle_index]

pairs = [["K", "L"], ["L", "M"], ["M", "N"], ["K", "O"], ["O", "P"]]
print(findLongestPathMiddleCourse(pairs))