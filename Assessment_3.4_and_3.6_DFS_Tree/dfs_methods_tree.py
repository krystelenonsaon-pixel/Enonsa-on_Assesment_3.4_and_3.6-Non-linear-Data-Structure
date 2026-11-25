"""
Assessment 3.6: DFS Methods in Tree

This program reuses the BinaryTree class from binary_tree.py (Assessment 3.4).
It builds the same Binary Search Tree using the unique letters E, N, O, S, A
from the last name "Enonsaon", then demonstrates the three DFS methods:
Pre-order, In-order, and Post-order.
"""

from binary_tree import BinaryTree


def build_existing_assessment_tree():
    # Keep the same letters and insertion order used in Assessment 3.4.
    letters = ["E", "N", "O", "S", "A"]

    tree = BinaryTree()
    for letter in letters:
        tree.insert(letter)

    return tree, letters


def main():
    tree, letters = build_existing_assessment_tree()

    print("====================================")
    print(" ASSESSMENT 3.6: DFS METHODS IN TREE")
    print("====================================")
    print("Source: Assessment 3.4 - Non-Linear Data Structure")
    print("Letters inserted:", letters)
    print()
    print("DFS Pre-order  (Root, Left, Right):", tree.dfs_preorder())
    print("DFS In-order   (Left, Root, Right):", tree.dfs_inorder())
    print("DFS Post-order (Left, Right, Root):", tree.dfs_postorder())


if __name__ == "__main__":
    main()
