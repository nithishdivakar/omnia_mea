---
layout: post
title:  "06a05__Binary Tree from its Traversals"
date:   2024-01-01 00:00:00 +0000
categories: 
status: todo
---

## Construct a binary tree from its in and pre prder traversals

```python
def build_tree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    val_to_idx = {val: idx for idx, val in enumerate(inorder)}

    def construct(in_left, in_right):
        if in_left > in_right:
            return None

        val = preorder.pop(0)
        in_idx = val_to_idx[val]
        node = TreeNode(val)

        node.left = construct(in_left, in_idx - 1)
        node.right = construct(in_idx + 1, in_right)
        return node

    return construct(0, len(preorder) - 1)
```
