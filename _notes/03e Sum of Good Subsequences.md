---
categories: null
date: 2024-01-01 00:00:00 +0000
index: 03e
layout: post
status: done
title: 03e Sum of Good Subsequences
---

## Sum of Good Subsequences [LC#3351]
> You are given an integer array nums. A good subsequence is defined as a subsequence of nums where the absolute difference between any two consecutive elements in the subsequence is exactly 1. Return the sum of all possible good subsequences of nums (modulo  $10^9 + 7$). Note that a subsequence of size 1 is considered good by definition.

**Intuition**

- We can append a number `a` to a sequence ending in `a-1` or `a+1` or start a new good subsequence, i.e,  `count[a] = count[a-1] + count[a+1] + 1`
- Contribution of `a` to the final sum is `a*count[a]`. But to avoid duplicates, we iterate over the array and keep the total in another counter

**Solution**

```python
def sum_of_good_subsequences(nums: List[int]) -> int:
    mod = 10 ** 9 + 7
    total = Counter()
    count = Counter()
    for a in nums:
        num_subseq_ending_at_a = count[a - 1] + count[a + 1] + 1
        
        total[a] += total[a - 1] + total[a + 1] + a * num_subseq_ending_at_a
        
        count[a] += num_subseq_ending_at_a
        
    return sum(total.values()) % mod
```

**Time Complexity**
- $T(n) = O(n)$; $S(n) = O(n)$