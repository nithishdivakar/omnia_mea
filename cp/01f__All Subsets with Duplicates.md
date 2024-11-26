## All Subsets with duplicates [LC#90]
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
