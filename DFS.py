graph = {
  'A': ['B', 'C','E','F'],
    'B': ['D','G','H'],
    'C': ['I','J'],
    'D': [],
    'E': ['K','L'],
    'F': ['M','N'],
    'G': [],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
}

visited = []

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for i in graph[node]:
            dfs(i)

dfs('A')
