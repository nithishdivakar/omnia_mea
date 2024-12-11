---
categories: null
date: 2024-01-01 00:00:00 +0000
index: 06c01
layout: post
status: done
title: 06c01 In a Binary Tree
---

## Lowest Common Ancestor of a Binary Tree [LC#236]
> Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”


### Code
```python
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowest_common_ancestor(root: "Node", p: "Node", q: "Node") -> "Node":
    def search(node):
        if node in [p, q, None]:
            return node
        left = search(node.left)
        right = search(node.right)
        if left and right:
            return node
        return left if left else right
    return search(root)
```

### Time complexity
$T(n) = O(n)$ and $S(n)= O(n)$ for the recursion stack in worst case.