
## Two sum [LC 1]
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

- Sorting and two pointers
    ```python
    def two_sum(nums: List[int], target:Int) -> Tuple[int, int]:
        A  = sorted([(n, i) for i, n in enumerate(nums)])
        left, right = 0, len(A) - 1
        
        while left < right:
            curr_sum = A[left][0] + A[right][0]
            if curr_sum == target: return (A[left][1], A[right][1])
            if curr_sum < target:
                left = left + 1
            else:
                right = right - 1
        return (-1, -1)

    ```
- Hashset
    ```python
    def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
        lut = {}
        for i, n in enumerate(nums):
            residue = target - n
            if residue in lut:
                return (i, lut[residue])
            lut[n] = i
        return (-1, -1)
    ```

## Maximum Subarray Sum [LC 53]
- Kadane's algorithm
- find the max sum of subarray ending at location `i`.
- $T(n) = O(n)$

```python
def max_subarray_sum(nums: List[int]) -> int:
    curr, ans = 0, nums[0]
    for num in nums:
        curr = max(curr + num, num)
        ans = max(ans, curr)
    return ans
```

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

## All Subsets with duplicates [LC 90]
- We consider elements with duplicate as 1 element
- when we need to add this element to subset, we add the on per each frequency
```python
def subsets_with_duplicates(self, nums: List[int]) -> List[List[int]]:
    ans = [[],]
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    for num, freq in freq.items():
        curr = []
        for subset in ans:
            for f in range(1, freq+1):
                new_subset = subset + [num]*f
                curr.append(new_subset)
        ans.extend(curr)
    return ans
```
