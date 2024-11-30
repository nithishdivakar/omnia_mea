---
categories: null
date: 2024-01-01 00:00:00 +0000
index: 01g
layout: post
title: 01g Median in a Stream
---
## Find Median from Data Stream [LC#295]
> The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
> - For example, for arr = [2,3,4], the median is 3.
> - For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.


```python
class MedianFinder:
    def __init__(self):
        self.low = [] # stores n or n+1 elements
        self.high = [] # stores n elements

    def add(self, num: int) -> None:
        val = heapq.heappushpop(self.low, -num)
        heapq.heappush(self.high, -val)
        if len(self.low) <  len(self.high):
            val = heapq.heappop(self.high)
            heapq.heappush(self.low, -val)

    def find_median(self) -> float:
        if len(self.low) > len(self.high):
            return - self.low[0]
        return (-self.low[0] + self.high[0])/2
```