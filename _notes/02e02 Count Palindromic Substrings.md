---
categories: null
date: 2024-01-01 00:00:00 +0000
index: 02e02
layout: post
status: done
title: 02e02 Count Palindromic Substrings
---

## Count Palindromic Substrings

```python
def count_palindromic_substrings(s: str) -> int:
    def expand_around_center(left: int, right: int) -> int:
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left = left - 1
            right = right + 1
            count = count + 1
        return count

    count = 0
    for i in range(len(s)):
        # odd length palindromes
        count += expand_around_center(i, i)

        # even length palindromes
        count += expand_around_center(i, i + 1)
    return count
```
- $T(n) = O(n^2)$
- $S(n) = O(1)$