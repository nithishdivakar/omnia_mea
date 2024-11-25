## Containers with most water [LC 11]
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
- Limiting factor of volume of water between 2 walls is the smaller one.
- Given a wall, once we find a farthest wall that is atleast same height or more, no other closer, taller wall could hold more water.
- So given 2 pairs of walls, we can move close from the smaller wall in hope to find a larger volume area
- $T(n) = O(n)$
```python
def max_water(height: List[int]) -> int:
    left, right = 0, len(height)-1
    max_area = 0
    while left < right:
        max_area = max(
            max_area, 
            (right - left)*(min(height[left], height[right])) 
        )
        # we have to move away from the smaller wall
        # as it is limiting factor of the area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area
```

