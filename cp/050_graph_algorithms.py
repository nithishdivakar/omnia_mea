

# Single Source Shortest Path
# graph = {
#   u: [(v, w_uv), ..]
#   ...
# }

distances = [math.inf] * n
distances[source] = 0
heap = [(0, source)]

while heap:
    curr_dist, node = heapq.heappop(heap)
    if curr_dist > distances[node]:
        continue
    
    for neighbour, weight in graph[node]:
        dist = curr_dist + weight
        if dist < distances[neighbour]:
            distances[neighbour] = dist
            heapq.heappush(heap, (dist, neighbour))
