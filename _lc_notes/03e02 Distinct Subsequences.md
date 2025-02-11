---
date: 2024-01-01 00:00:00 +0000
slug: '03e02'
layout: post
status: done
title: Distinct Subsequences
tags: []
---

## Distinct Subsequences [LC#115]
> Given two strings `s` and `t`, return the number of distinct subsequences of `s` which equals `t`.

### Intuition

### Code
```python
def distinct_subsequences(s: str, t: str) -> int:
    m = len(s) # i
    n = len(t) # j
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        if s[i] == t[0]:
            dp[i][0] = 1

    for j in range(1, n):
        running_sum = dp[0][j - 1]
        for i in range(1, m):
            if s[i] == t[j]:
                # dp[i][j] = sum(dp[k][j - 1] for k in range(i))
                dp[i][j] = running_sum
            running_sum += dp[i][j - 1]

    return sum(dp[i][n - 1] for i in range(m))

OR
def distinct_subsequences(s: str, t: str) -> int:
    m = len(s) # i
    n = len(t) # j
    dp = [[0] * (n+1) for _ in range(m+1)]

    dp[0][0] = 1

    for i in range(1, m+1):
        dp[i][0] = 1
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j]
            if s[i-1] == t[j-1]:
                dp[i][j] += dp[i-1][j - 1]
    return dp[m][n]
```

### Time complexity
- $T(n) = O(mn)$ 
- $S(n) = O(mn)$ but can be space optimised to $O(n)$
