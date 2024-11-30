---
categories: array stack
date: 2024-01-01 00:00:00 +0000
index: '01i01'
layout: post
status: done
title: 01i01 Largest Rectangle in Histogram
---


## Largest Rectangle in Histogram [ LC# 84]
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

**Brute Force**
- Enumerate every range. Compute the Area
- $T(n) = O(n^2)$; $S(n) = O(n^2)$

```python
area[i][j] = min_heights[i:j] * ( j-i+1 )
min_heights[i:j] = min(min_heights[i-1:j-1], heights[i], heights[j])
min_heights[i:i] = heights[i]
```

**Monotonic Stack**
- Consider all the rectangles where height[i] is its right side. 
- Maintain a stack such that heights in the stack are always in increasing order.
- When we see a column that is higher than what is on the stack, use it as the right side and compute all the possible rectangles using what is on the stack to derive left side and height.
- Remove each considered rectangle / column from the stack
- $T(n) = O(n)$; $S(n) = O(n)$

```python
def largest_rectangle_in_historgam(heights: List[int]) -> int:
    stack = [-1] # monotonic stack which maintains no decreasing heights till i
    max_area = 0
    
    heights.append(0)
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            mid = stack.pop()
            left = stack[-1] + 1
            right = i
            max_area = max(max_area,  heights[mid] * (right - left))
        stack.append(i)
    return max_area
```