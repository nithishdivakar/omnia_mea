+++
title = '05f__Detecting a Cycle in Linked List'
date = 2024-11-14T07:07:07+01:00
draft = false
+++
  
## Cycle detection
- Turtle and hare algorithm
It relies on the fact that if two pointers are moving at different speeds within a cycle, their distances will reach a max length before being reset to zero at which point they will point to the same element. 
- $T(n) = O(n)$ Will travel initial `n` of non-cyclic then `k` which is cycle length.
- $S(n) = O(n)$
```python
def has_cycle(head: Optional[ListNode]) -> bool:
    turtle, hare = ListNode(0, head), ListNode(0, head)
    while turtle and hare:
        if turtle == hare:
            return True
        turtle = turtle.next
        hare = hare.next.next if hare.next else None
    return False
```
