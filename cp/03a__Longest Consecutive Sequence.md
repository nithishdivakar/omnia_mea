## Longest Consecutive Sequence [LC#128]
- For each num, if num-1 is not in the list, then its possibly a sequence's begning
- For each sequence begning, check if conseqtive elements are in the list
- Each valid sequence is tested once
```python
def longestconsecutive_sequence(nums: List[int]) -> int:
    entries = set(nums)
    best = 0
    for num in nums:
        if num-1 not in entries:
            next_num, seq_len = num+1, 1
            while next_num in entries: 
                next_num += 1
                seq_len += 1
            best = max(best, seq_len)
    return best
```
- $T(n) = O(n)$
- $S(n) = O(n)$