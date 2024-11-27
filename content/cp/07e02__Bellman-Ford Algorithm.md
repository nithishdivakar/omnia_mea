+++
title = '07e02__Bellman-Ford Algorithm'
date = 2024-11-14T07:07:07+01:00
draft = false
+++
  
## Bellman-Ford
```python
def bellman_ford(graph, source):
    # Initialize distances from source to all vertices as INFINITE
    distances = {v: float("inf") for v in graph}
    distances[source] = 0  # Distance from source to itself is always 0

    # Relax all edges |V| - 1 times
    for _ in range(len(graph) - 1):
        for u in graph:
            for v, w in graph[u]:
                if distances[u] != float("inf") and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

    # Check for negative-weight cycles
    for u in graph:
        for v, w in graph[u]:
            if distances[u] != float("inf") and distances[u] + w < distances[v]:
                print("Graph contains negative weight cycle")
                return None

    return distances
```