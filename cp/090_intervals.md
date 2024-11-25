


## Min meeting rooms
We are given meeting times in intervals. Find minimum no of meeting rooms required.

- Sort by start time
- Keep all the overlapping ending times in a min heap
- If the top ending time is past, you can pop it.

```python
def min_meeting_rooms(intervals: List[List[int]]) -> int:
    intervals = sorted(intervals)
    heap = [intervals[0][1]]  # first end time
    meeting_rooms = 1
    for start_time, end_time in intervals[1:]:
        if start_time >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, end_time)
        meeting_rooms = max(meeting_rooms, len(heap))
    return meeting_rooms
```
- $T(n)  = O(n log n + n log n)$ sorting + n pops
- $S(n) = O(n)$
