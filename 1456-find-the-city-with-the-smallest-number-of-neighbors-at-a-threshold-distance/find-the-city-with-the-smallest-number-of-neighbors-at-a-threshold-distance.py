class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w

        # Floyd-Warshall: try every city as an intermediate point
        for mid in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][mid] + dist[mid][j] < dist[i][j]:
                        dist[i][j] = dist[i][mid] + dist[mid][j]

        best_city = -1
        min_count = float('inf')

        for i in range(n):
            count = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
            if count <= min_count:
                min_count = count
                best_city = i

        return best_city