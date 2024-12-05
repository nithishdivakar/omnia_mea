---
categories: null
date: 2024-01-01 00:00:00 +0000
index: 09b
layout: post
status: doing
title: 09b Unbounded Knapsack
---

## Unbounded Knapsack

```python
def unbounded_knapsack(weights: List[int], values: List[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)
    for i in range(1, capacity + 1):
        for j in range(len(weights)):
            if weights[j] <= i:
                dp[i] = max(dp[i], dp[i - weights[j]] + values[j])
    return dp[capacity]
```