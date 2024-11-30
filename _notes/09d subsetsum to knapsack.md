---
categories: null
date: 2024-01-01 00:00:00 +0000
index: 09d
layout: post
status: doing
title: 09d subsetsum to knapsack
---

## Reducing subset sum to 0/1 knapsack

```python
def subset_sum(nums: List[int], target: int) -> bool:
    max_value = knapsack_01(nums, nums, target)
    return max_value == target

def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    max_value = [0] * (capacity + 1)

    for weight, value in zip(weights, values):
        for slack in range(capacity, weight - 1, -1):
            max_value[slack] = max(max_value[slack], max_value[slack - weight] + value)

    return max_value[capacity]
```