
## Longest Increasing Subsequence

1. Dynamic programming approach

    > Find the length of longest increasing subsequence ending at i. 
    ```python
    def length_of_lis(nums: List[int) -> int:
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
    
    def length_of_LIS(nums):
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
