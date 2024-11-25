
## Longest Increasing Subsequence

1. Dynamic programming approach

    > Find the length of longest increasing subsequence ending at i. 
    ```python
    def length_of_lis(nums: List[int]) -> int:
        if not nums: return 0
        max_length = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    max_length[i] = max(max_length[i], max_length[j] + 1)
        return max(max_length)
    ```

2. Technique based on [patience sorting](https://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence.pdf)
    - If the number is larger than the largest element in the temporary array, append it. Otherwise, replace the found position with the current number.
    - The length of the temporary array will give the length of the longest increasing subsequence.
    - the tem array may not always have a valid subsequence, but its length will always be equal to longest subsequence.
    ```python
    from bisect import bisect_left
    
    def length_of_LIS(nums: List[int]) -> int:
        if not nums: return 0
        tails = []
        for num in nums:
            pos = bisect_left(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)
    ```

## Longest Common Subsequence

1. Dynamic programming approach
    -  `dp[i][j]` contains length of longest subsequence by using first `i-1` characters of first string and `j-1` characters of second string.
    -  `dp[i][0] = 0` and `dp[0][j] = 0`
    ```python
    def longest_common_subsequence(X, Y) -> int:
        m = len(X)
        n = len(Y)
        
        # Create a 2D array to store lengths of longest common subsequence.
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Build the dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The length of the longest common subsequence is in dp[m][n]
        return dp[m][n]

    ```
    - $T(n) = O(mn)$
    - $S(n) = O(mn)$
    

3. with space optimisation
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
    - $T(n) = O(mn)$
    - $S(n) = O(\min\\{m,n\\})$
