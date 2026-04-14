[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/mHMwxQwH)
# Weekly Coding #5: Skyrail Station Navigator

## Summary
This program implements a binary tree node structure and five core tree operations for navigating a Skyrail station map. The three traversal functions — preorder, inorder, and postorder — each recursively walk the tree and collect node values in a different order. The two BST functions implement search and insertion using the BST ordering property, where left subtree values are smaller and right subtree values are larger than the current node.

---

## Approach
- **Preorder traversal:** Visit the current node first, then recurse left, then recurse right. The base case returns `[]` for a `None` node. Results are built by concatenating three lists: `[root.value]`, the left subtree result, and the right subtree result.
- **Inorder traversal:** Recurse left first, then visit the current node, then recurse right. Same base case. This order produces sorted output when the tree is a valid BST.
- **Postorder traversal:** Recurse left and right first, then visit the current node last. Useful conceptually for bottom-up processing.
- **BST search (`bst_contains`):** At each node, compare the target to `root.value`. Return `True` if equal, recurse left if smaller, recurse right if larger. Return `False` when `None` is reached.
- **BST insert (`bst_insert`):** Navigate the same way as search. When a `None` slot is reached, create and return a new `TreeNode`. Duplicate values are silently ignored via the `elif value > root.value` guard — only strict inequality triggers a recursive call.

---

## Complexity

### `preorder_values`
- **Time:** O(n)
- **Space:** O(n)
- **Why:** Every node is visited exactly once, producing one value in the output list. The call stack depth equals the tree height (O(log n) balanced, O(n) worst case), and the returned list always holds all n values.

### `inorder_values`
- **Time:** O(n)
- **Space:** O(n)
- **Why:** Same reasoning as preorder — every node is visited once and contributes one element to the output list.

### `postorder_values`
- **Time:** O(n)
- **Space:** O(n)
- **Why:** Same reasoning — all n nodes are visited and all n values are collected regardless of traversal order.

### `bst_contains`
- **Time:** O(h) where h is tree height — O(log n) average, O(n) worst case (skewed tree)
- **Space:** O(h) for the recursive call stack
- **Why:** Each comparison eliminates one subtree, so only one root-to-leaf path is followed. No list is built; stack depth is the only extra space used.

### `bst_insert`
- **Time:** O(h) — O(log n) average, O(n) worst case
- **Space:** O(h) for the call stack
- **Why:** Like search, only one path is followed from root to the insertion point. A single new node is created at the end; the rest of the tree is untouched.

---

## Edge-Case Checklist
- [x] **Empty tree traversal returns `[]`** — All three traversal functions return `[]` immediately when `root is None`.
- [x] **Single-node traversal works correctly** — A leaf node has `None` children, so both recursive calls return `[]`, leaving only `[root.value]` in the result.
- [x] **`bst_contains` returns `False` for an empty tree** — The first check `if root is None: return False` handles this.
- [x] **`bst_contains` returns `False` when the target is missing** — The search follows BST paths until hitting `None`, at which point it returns `False`.
- [x] **`bst_insert` creates a root when the tree is empty** — `if root is None: return TreeNode(value)` handles this as the base case, returning a fresh node with no children.
- [x] **`bst_insert` ignores duplicate values** — Only `<` and `>` trigger recursive calls; an equal value falls through to `return root` with no modification.
- [x] **Deeper insert case tested** — Inserting 55 into the sample BST navigates to the right subtree (60), then left (50), then right of 50, placing 55 correctly. Verified with `inorder_values` producing `[10, 20, 30, 40, 50, 55, 60, 70]`.

---

## Assistance & Sources
- **AI used? (Y/N):** Y
- **What AI helped with:** Claude (Anthropic) was used to write and verify all five function implementations.
- **Other sources used:** None

---

## Test Results