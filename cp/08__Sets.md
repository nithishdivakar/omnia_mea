
## Subsets II [LC#90]
Given an integer array nums that may contain duplicates, return all possible  subsets (the power set). The solution set must not contain duplicate subsets. Return the solution in any order.

- $T(n) = O(2^n)$; $S(n) = O(2^n)$

```python
def subsets_of_multiset(nums: List[int]) -> List[List[int]]:
    powerset = [[],]
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0)+1

    for num, num_freq in freq.items():
        curr = []
        for subset in ans:
            for ff in range(1, num_freq + 1):
                new_subset = subset + [num] * ff
                curr.append(new_subset)
        powerset.extend(curr)
    return powerset
```
