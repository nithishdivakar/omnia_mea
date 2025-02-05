---
date: 2024-01-01 00:00:00 +0000
layout: post
slug: 07a
status: done
title: BFS
---

## BFS

Template

```python
def bfs():
    queue = deque()
    seen = set()
    queue.append(start_node)
    seen.add(start_node)
    while queue:
        node = queue.popleft()
        for neigh in neighbors(node):
            if neigh not in seen:
                visit(neigh)
                queue.append(neigh)
                seen.add(neigh)
```