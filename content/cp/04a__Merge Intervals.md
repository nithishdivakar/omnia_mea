+++
title = '04a__Merge Intervals'
date = 2024-11-14T07:07:07+01:00
draft = false
+++
## Merge Intervals [LC#56]
Given an array of intervals where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

**Sort and Itrate approach**
- Sort the intervals by start time
- Iterate over the intervals one by on merging the current with the previous if there is an overlap
- $T(n) = O(n log n + n)$; $S(n) = O(n)$
```python
def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals)
    ans = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], end)
        else:
            ans.append([start, end])
    return ans
```
