from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': [],
    'D': []
}

visited = []
queue = deque(['A'])

while queue:
    node = queue.popleft()
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        queue.extend(graph[node])