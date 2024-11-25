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
