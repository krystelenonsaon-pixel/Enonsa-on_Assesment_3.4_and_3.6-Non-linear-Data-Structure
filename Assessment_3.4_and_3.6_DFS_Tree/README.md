# Assessment 3.4 + Assessment 3.6

This folder keeps the Assessment 3.4 non-linear data structure programs and
adds a separate program for Assessment 3.6: DFS Methods in Tree.

## Files

- `binary_tree.py` — Binary Search Tree implementation from the earlier assessment, including BFS and DFS methods.
- `graph.py` — Graph implementation from the earlier assessment, including BFS and DFS.
- `dfs_methods_tree.py` — New Assessment 3.6 program. It imports and reuses `BinaryTree` from `binary_tree.py`.
- `Algorithm_Assessment_3.6.md` — Algorithm and expected output for the new task.

## Connection between the assessments

The new DFS program uses the same tree class, letters, and insertion order as
the earlier tree program: `E, N, O, S, A` from `Enonsaon`. It does not create
an unrelated tree or change the previous data.

## Run the programs

Run these commands from this folder:

```bash
python binary_tree.py
python graph.py
python dfs_methods_tree.py
```

For Assessment 3.6, the important command is:

```bash
python dfs_methods_tree.py
```

Make sure `binary_tree.py` and `dfs_methods_tree.py` stay in the same folder
because the new program imports the `BinaryTree` class from that file.
