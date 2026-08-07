import heapq
from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total=0
        heap=[(0,0)]
        visited = []
        size=len(points)
        while len(visited)<size:
            c,n=heapq.heappop(heap)
            if n in visited:
                continue
            total+=c
            visited.append(n)
            x1,y1=points[n]
            for i in range(size):
                if i not in visited:
                    x2,y2=points[i]
                    dis=abs(x1-x2)+abs(y1-y2)
                    heapq.heappush(heap,(dis,i))
        return total