

## Longest Substring Without Repeating Characters [LC 3]

- Sliding Window (2 pointers)
    - Keep track of character counts. Whenever a character count goes more than 1, retract the window until count goes below 1   
        ```python
        def max_substring_without_repetition(s: str) -> int:
             ans = 0
             char_count = defaultdict(int)
             left = 0
             for right in range(len(s)):
                 current_char = s[right]
                 char_count[current_char] += 1 
                 while char_count[current_char]>1:
                     char_count[s[left]] -= 1 
                     left += 1
                 ans = max(ans, right-left+1)
             return ans
        ```
- Optimised Sliding window
    - keep track of where each characters were last found at.
    - When a character is encountered a second time, use the look up table to jump ahead
        ```python
        def max_substring_without_repetition(s: str) -> int:
            last_found_at = {}
            left = 0
            ans = 0
            for right in range(len(s)):
                current_char = s[right]
                if current_char in last_found_at:
                    left = max(left, last_found_at[current_char]+1)
                last_found_at[current_char] = right
                ans = max(ans, right - left +1)
            return ans
        ```

## Edit distance
- `cost[i][j]` = the minimum edit distance (or the minimum number of operations) required to transform the first i characters of word1 into the first j characters of word2.
```python
def edit_distance(word1: str, word2: str) -> int:
    # Define the costs for operations
    costs = {'insert': 1, 'delete': 1, 'substitute': 1}
    m, n = len(word1), len(word2)
    
    cost = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row and column
    for i in range(m + 1):
        cost[i][0] = i  # Cost of deleting all characters from word1 to form word2
    for j in range(n + 1):
        cost[0][j] = j  # Cost of inserting all characters to word1 to form word2

    # Fill the cost matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                cost[i][j] = cost[i - 1][j - 1]  # No operation needed
            else:
                cost[i][j] = min(
                    cost[i - 1][j] + costs['insert'],      # Insert
                    cost[i][j - 1] + costs['delete'],      # Delete
                    cost[i - 1][j - 1] + costs['substitute']  # Substitute
                )
    return cost[m][n]
```
- $T(n) = O(mn)$
- $S(n) = O(mn)$ but can be optimised to $O(\min(m,n))$
