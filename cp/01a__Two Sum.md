## Two sum [LC#1]
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

- Sorting and two pointers
    ```python
    def two_sum(nums: List[int], target:Int) -> Tuple[int, int]:
        A  = sorted([(n, i) for i, n in enumerate(nums)])
        left, right = 0, len(A) - 1
        
        while left < right:
            curr_sum = A[left][0] + A[right][0]
            if curr_sum == target: return (A[left][1], A[right][1])
            if curr_sum < target:
                left = left + 1
            else:
                right = right - 1
        return (-1, -1)

    ```
- Hashset
    ```python
    def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
        lut = {}
        for i, n in enumerate(nums):
            residue = target - n
            if residue in lut:
                return (i, lut[residue])
            lut[n] = i
        return (-1, -1)
    ```

