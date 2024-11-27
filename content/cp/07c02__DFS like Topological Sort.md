+++
title = '07c02__DFS like Topological Sort'
date = 2024-11-14T07:07:07+01:00
draft = false
+++


## DFS like topological sort
```python
def topological_sort_dfs(graph: Dict[str, List[str]]) -> List[str]:
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}
    stack: List[str] = []

    def dfs(node: str) -> bool:
        if color[node] == GRAY:
            return []  # Cycle detected
        if color[node] == WHITE:
            color[node] = GRAY
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    # cycle in recursion
                    return False
            color[node] = BLACK
            stack.append(node)
        return True

    for vertex in graph:
        if color[vertex] == WHITE:
            if not dfs(vertex):  # If a cycle is detected
                return []

    return stack[::-1]
```
