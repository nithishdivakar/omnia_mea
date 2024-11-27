+++
title = '05c__Merging Two Sorted Linked Lists'
date = 2024-11-14T07:07:07+01:00
draft = false
+++
## Merge Two Sorted Lists [LC#21]

You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
```
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
```

**Iterate and Merge**
- $T(n) = O(m+n)$; $S(n) = O(1)$

```python
def merge_two_worted_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      fake_head = ListNode()
      current = fake_head
      
      while list1 and list2:
          if list1.val < list2.val:
              current.next = list1
              list1 = list1.next
          else:
              current.next = list2
              list2 = list2.next
          current = current.next
      current.next = list1 if list1 else list2
      
      return fake_head.next
```        
