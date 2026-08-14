class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n + 1))  # nodes are 1-indexed

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False  # already connected -> this edge creates a cycle
            parent[rx] = ry
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]