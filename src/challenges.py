"""Weekly Coding #5 starter code: Trees, traversals, and BST basics."""

from __future__ import annotations

from typing import Any


class TreeNode:
    """A simple binary tree node."""

    def __init__(
        self,
        value: Any,
        left: TreeNode | None = None,
        right: TreeNode | None = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


def preorder_values(root: TreeNode | None) -> list[Any]:
    """Return the tree values in preorder: node, left, right."""
    if root is None:
        return []
    return [root.value] + preorder_values(root.left) + preorder_values(root.right)


def inorder_values(root: TreeNode | None) -> list[Any]:
    """Return the tree values in inorder: left, node, right."""
    if root is None:
        return []
    return inorder_values(root.left) + [root.value] + inorder_values(root.right)


def postorder_values(root: TreeNode | None) -> list[Any]:
    """Return the tree values in postorder: left, right, node."""
    if root is None:
        return []
    return postorder_values(root.left) + postorder_values(root.right) + [root.value]


def bst_contains(root: TreeNode | None, target: int) -> bool:
    """Return True if target exists in the BST. Otherwise return False."""
    if root is None:
        return False
    if target == root.value:
        return True
    elif target < root.value:
        return bst_contains(root.left, target)
    else:
        return bst_contains(root.right, target)


def bst_insert(root: TreeNode | None, value: int) -> TreeNode:
    """Insert value into the BST and return the root node.

    Duplicate values should be ignored.
    """
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = bst_insert(root.left, value)
    elif value > root.value:
        root.right = bst_insert(root.right, value)
    # If value == root.value, it's a duplicate — do nothing
    return root


# --- Quick tests ---
if __name__ == "__main__":
    #       4
    #      / \
    #     2   6
    #    / \ / \
    #   1  3 5  7
    root = TreeNode(4,
        TreeNode(2, TreeNode(1), TreeNode(3)),
        TreeNode(6, TreeNode(5), TreeNode(7)),
    )

    print("Preorder: ", preorder_values(root))   # [4, 2, 1, 3, 6, 5, 7]
    print("Inorder:  ", inorder_values(root))    # [1, 2, 3, 4, 5, 6, 7]
    print("Postorder:", postorder_values(root))  # [1, 3, 2, 5, 7, 6, 4]

    bst = None
    for v in [5, 3, 7, 1, 4]:
        bst = bst_insert(bst, v)

    print("\nbst_contains(bst, 4):", bst_contains(bst, 4))   # True
    print("bst_contains(bst, 6):", bst_contains(bst, 6))    # False
    bst = bst_insert(bst, 4)   # duplicate — ignored
    print("Inorder after duplicate insert:", inorder_values(bst))  # [1, 3, 4, 5, 7]