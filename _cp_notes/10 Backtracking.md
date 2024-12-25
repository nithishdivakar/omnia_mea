---
date: 2024-01-01 00:00:00 +0000
index: '10'
layout: post
status: done
title: 10 Backtracking
---

# Backtracking

Code template
```python
ans = []
def backtrack(state):
    if is_valid(state):
        ans.append(state)
        # return

    for candidate in get_candidates(state):
        new_state = state + candidate
        backtrack(new_state)
```