---
categories: null
date: 2024-01-01 00:00:00 +0000
index: 05a
layout: post
status: done
title: 05a Reverse Linked List
---

## Reverse Linked List [LC#206]
> Given the head of a singly linked list, reverse the list, and return the reversed list.

**Iterative approach**

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
### Time Complexity
- $T(n) = O(n)$
- $S(n) = O(1)$