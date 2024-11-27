---
layout: post
title:  "05a__Reversing a Linked List"
date:   2024-01-01 00:00:00 +0000
categories: 
---


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

