+++
title = '01h__Binary Search'
date = 2024-11-14T07:07:07+01:00
draft = false
+++
# I.
# Binary search pattern when we are searching for a target
# in an ordered array with element w.r.to target like                                                     
#       ┌───────────┬───┬────────────┐      
#       │     <     │ = │     >      │      
#       └───────────┴───┴────────────┘                                  

```python
L, R = 0, N-1

while L <= R:
  mid = L + (R-L)//2
  if a[mid] == target:
    return mid
  if a[mid] > target:
    R = mid - 1
  else:
    L = mid + 1
return -1
```

# II.
# Binary search pattern when we are searching for
# the first/smallest valid position when the array is like                                   
#   ┌───┬───┬───┬───┬───┬───┬───┬───┐      
#   │ f │ f │ f │ t │ t │ t │ t │ t │     
#   └───┴───┴───┴───┴───┴───┴───┴───┘   
#                 └── ans 

```python
L, R = 0, N-1
ans = -1

while L <= R:
  mid = L + (R-L)//2
  if is_valid(mid):
    ans = mid
    R = mid - 1
  else:
    L = mid + 1
return ans
```