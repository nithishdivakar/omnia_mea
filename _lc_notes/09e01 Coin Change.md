---
date: 2024-01-01 00:00:00 +0000
slug: '09e01'
layout: post
status: done
title: Coin Change
tags: [knapsack]
---

## Coin Change [LC#322]
> You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1. You may assume that you have an infinite number of each kind of coin.

### Intuition


### Code
```python
def coin_change(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1 
```

### Time complexity
- $T(n) = O(nW)$ 
- $S(n) = O(W)$
