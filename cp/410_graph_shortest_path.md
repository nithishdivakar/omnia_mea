

# Single Source Shortest Path

## Dijkstra algorithm

- `graph = {u : [(v, w(u,v)), ..], ... }`
```python
def dijkstra(graph: List[List[Tuple[int, float]]], source: int) -> List[float]:
    n = len(graph)
    distances: List[float] = [math.inf] * n
    distances[source] = 0.0
    heap: List[Tuple[float, int]] = [(0.0, source)]

    while heap:
        curr_dist, node = heapq.heappop(heap)
        if curr_dist > distances[node]:
            continue
        
        for neighbour, weight in graph[node]:
            dist = curr_dist + weight
            if dist < distances[neighbour]:
                distances[neighbour] = dist
                heapq.heappush(heap, (dist, neighbour))
    
    return distances
```
- $T(n) = O( (V+E) \log V)$
    - $O(V \log\{V\})$: Extract the minimum node from the heap for each vertex.
    - $O(E \log\{V\})$: Time taken to insert or update distances for each edge.    
- $S(n) = O(V)$


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