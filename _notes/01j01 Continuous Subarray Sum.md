---
categories: null
date: 2024-01-01 00:00:00 +0000
index: 01j
layout: post
status: done
title: 01j01 Continuous Subarray Sum
---

## Continuous Subarray Sum [LC#523]
> Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise. A good subarray is a subarray where:
> - Its length is at least two, and
> - The sum of the elements of the subarray is a multiple of k.


**Intuition**
- For quickly finiding sum of a subarray, we can use prefix sums. 
    - `sum([i,j]) = prefix(i) - prefix(j)`
- mod operator preoperty:  
    - `sum([i,j])%k = (prefix(i) - prefix(j))%k = (prefix(i)%k - prefix(j)%k)%k`
- So if `prefix(i)%k == prefix(j)%k` for any `i` and `j` more than 2 indeices apart, the answer is true.
- Only corner case is a prefix array sum itself that `sum%k` to 0.

**Solution**

```python
def checkSubarraySum(nums: List[int], k: int) -> bool:
    n = len(nums)
    mod_seen = {0: -1}  # for prefixes that exactly sum%k to 0
    prefix_sum = 0
    for i in range(n):
        prefix_sum = prefix_sum + nums[i]
        prefix_mod = prefix_sum % k
        if prefix_mod in mod_seen and i - mod_seen[prefix_mod] > 1:
            return True
        else:
            mod_seen[prefix_mod] = i

        prefix_sum = prefix_mod
    return False

```
**Time Complexity**
- $T(n) = O(n)$ $S(n) = O(n)$