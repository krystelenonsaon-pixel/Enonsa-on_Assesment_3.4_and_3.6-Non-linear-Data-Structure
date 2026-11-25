"""
Assessment 3.4: Non-Linear Data Structure
Undirected graph built from the unique letters of "Enonsaon".
"""

class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = []

    def add_edge(self, vertex_a, vertex_b):
        self.add_vertex(vertex_a)
        self.add_vertex(vertex_b)

        if vertex_b not in self.adjacency[vertex_a]:
            self.adjacency[vertex_a].append(vertex_b)
        if vertex_a not in self.adjacency[vertex_b]:
            self.adjacency[vertex_b].append(vertex_a)

    def bfs(self, start):
        visited = {start}
        queue = [start]
        result = []

        while queue:
            current = queue.pop(0)
            result.append(current)

            for neighbor in sorted(self.adjacency[current]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def dfs(self, start):
        visited = set()
        result = []
        self._dfs_recursive(start, visited, result)
        return result

    def _dfs_recursive(self, vertex, visited, result):
        visited.add(vertex)
        result.append(vertex)

        for neighbor in sorted(self.adjacency[vertex]):
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited, result)


if __name__ == "__main__":
    graph = Graph()
    edges = [("E", "N"), ("N", "O"), ("N", "S"), ("S", "A"), ("A", "O")]

    for first, second in edges:
        graph.add_edge(first, second)

    print("Vertices:", list(graph.adjacency.keys()))
    print("Edges:", edges)
    print("BFS from E:", graph.bfs("E"))
    print("DFS from E:", graph.dfs("E"))
