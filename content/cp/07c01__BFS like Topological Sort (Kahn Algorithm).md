+++
title = '07c01__BFS like Topological Sort (Kahn Algorithm)'
date = 2024-11-14T07:07:07+01:00
draft = false
+++
  
## Kahn's Algorithm (BFS-like)

```python
def topological_sort_kahn(graph: Dict[str, List[str]]) -> List[str]:
    in_degree = {u: 0 for u in graph}  # Initialize in-degrees to 0
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1  # Increment in-degree for each edge

    queue = deque([u for u in in_degree if in_degree[u] == 0])
    topological_order = []

    while queue:
        u = queue.popleft()  # Get a vertex with in-degree 0
        topological_order.append(u)  # Add it to the topological order
        
        for v in graph[u]:
            in_degree[v] -= 1  # Remove the edge u -> v
            if in_degree[v] == 0:  # If in-degree becomes 0, add to queue
                queue.append(v)

    if len(topological_order) != len(graph):
        return []
    return topological_order
```

**Example Graph**
```
graph = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['E'],
    'E': []
}
```