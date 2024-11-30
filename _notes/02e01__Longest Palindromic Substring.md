---
categories: null
date: 2024-01-01 00:00:00 +0000
index: 02e01
layout: post
title: 02e01 Longest Palindromic Substring
---

## Longest Palindromic Substring

Expand around Center
```python
def longestPalindrome(string: str) -> str:
    def expand_around_center(left: int, right: int, string: str) -> str:
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left = left - 1
            right = right + 1
        return string[left + 1 : right]

    longest = ""
    for i in range(len(s)):
        longest = max(
            longest,
            expand_around_center(i, i, string),
            expand_around_center(i, i + 1, string),
            key=len,
        )
    return longest
```
- $T(n) = O(n^2)$
- $S(n) = O(1)$