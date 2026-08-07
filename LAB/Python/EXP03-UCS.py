import heapq

graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 3), ('E', 6)],
    'C': [('F', 5)],
    'D': [('G', 4)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

def ucs(start, goal):
    pq = [(0, start, [start])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)

        if node == goal:
            print("Path:", " -> ".join(path))
            print("Cost:", cost)
            return

        if node not in visited:
            visited.add(node)

            for neighbor, weight in graph[node]:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))

ucs('A', 'G')
