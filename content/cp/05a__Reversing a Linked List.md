+++
title = '05a__Reversing a Linked List'
date = 2024-11-14T07:07:07+01:00
draft = false
+++
# Reversing a linked list iterative

```python
def fn(head):
    curr = head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node 
        
    return prev
```

