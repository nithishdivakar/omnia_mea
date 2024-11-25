

### Longest Palindromic Substring

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

### Count Palindromic Substrings
```python
def count_palindromic_substrings(self, s: str) -> int:
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
