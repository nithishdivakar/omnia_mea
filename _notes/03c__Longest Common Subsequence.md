---
layout: post
title:  "03c__Longest Common Subsequence"
date:   2024-01-01 00:00:00 +0000
categories: 
---

  
## Longest Common Subsequence

**Dynamic programming approach**
-  `dp[i][j]` contains length of longest subsequence by using first `i-1` characters of first string and `j-1` characters of second string.
-  `dp[i][0] = 0` and `dp[0][j] = 0`
- $T(n) = O(mn)$; $S(n) = O(mn)$
    ```python
    def longest_common_subsequence(text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        
        # Create a 2D array to store lengths of longest common subsequence.
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Build the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The length of the longest common subsequence is in dp[m][n]
        return dp[m][n]
    ```
    
**Dynamic programming approach with space optimisation**
- $T(n) = O(mn)$ ; $S(n) = O(\min\\{m,n\\})$
    ```python
    def longest_common_subsequence(text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            return longest_common_subsequence(text2, text1)

        m = len(text1)
        n = len(text2)

        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    curr[j] = prev[j - 1] + 1
                else:
                    curr[j] = max(curr[j - 1], prev[j])
            prev, curr = curr, prev
        return prev[n]
    ```