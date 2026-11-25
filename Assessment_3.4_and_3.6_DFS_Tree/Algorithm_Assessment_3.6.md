# Assessment 3.6: DFS Methods in Tree

## Connection to Assessment 3.4

This program uses the same Binary Search Tree structure from Assessment 3.4.
It imports the `BinaryTree` class from `binary_tree.py`, then inserts the same
unique letters from the last name **Enonsaon** in the same order:

`E, N, O, S, A`

The tree is not replaced with a different example. Assessment 3.6 reuses the
existing tree-building logic and focuses on its Depth-First Search (DFS)
traversal methods.

## Algorithm

1. Start the program.
2. Import the `BinaryTree` class from `binary_tree.py`.
3. Create an empty Binary Search Tree.
4. Store the letters `E, N, O, S, A` in their original insertion order.
5. Insert each letter into the Binary Search Tree.
6. Perform DFS Pre-order:
   - Visit the root node.
   - Traverse the left subtree.
   - Traverse the right subtree.
7. Perform DFS In-order:
   - Traverse the left subtree.
   - Visit the root node.
   - Traverse the right subtree.
8. Perform DFS Post-order:
   - Traverse the left subtree.
   - Traverse the right subtree.
   - Visit the root node.
9. Display the three traversal results.
10. End the program.

## Expected Output

```text
====================================
 ASSESSMENT 3.6: DFS METHODS IN TREE
====================================
Source: Assessment 3.4 - Non-Linear Data Structure
Letters inserted: ['E', 'N', 'O', 'S', 'A']

DFS Pre-order  (Root, Left, Right): ['E', 'A', 'N', 'O', 'S']
DFS In-order   (Left, Root, Right): ['A', 'E', 'N', 'O', 'S']
DFS Post-order (Left, Right, Root): ['A', 'S', 'O', 'N', 'E']
```

## How to Run

Keep `binary_tree.py` and `dfs_methods_tree.py` in the same folder, then run:

```bash
python dfs_methods_tree.py
```

The `graph.py` file is retained from Assessment 3.4 and is not needed to run
the tree DFS program.
