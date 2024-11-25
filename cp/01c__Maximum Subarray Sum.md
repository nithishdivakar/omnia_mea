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

