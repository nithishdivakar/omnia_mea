
## Min meeting rooms
We are given meeting times in intervals. Find minimum no of meeting rooms required.

- Sort all meetings by their start time
- Keep the ending times of currently occupied meeting rooms in the min heap
- If current start time is earlier than the min heap end time, we need a new room else we can pop the top and add a new room

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
