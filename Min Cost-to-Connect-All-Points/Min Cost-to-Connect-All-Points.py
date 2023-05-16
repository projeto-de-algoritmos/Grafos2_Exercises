class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(parent, i):
            if parent[i] == i:
                return i
            return find(parent, parent[i])

        def union(parent, rank, x, y):
            x_root = find(parent, x)
            y_root = find(parent, y)
            if rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            elif rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1

        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                xi, yi = points[i]
                xj, yj = points[j]
                cost = abs(xi - xj) + abs(yi - yj)
                edges.append((cost, i, j))

        edges.sort()
        parent = [i for i in range(n)]
        rank = [0] * n
        min_cost = 0
        num_edges = 0

        for cost, i, j in edges:
            if find(parent, i) != find(parent, j):
                union(parent, rank, i, j)
                min_cost += cost
                num_edges += 1
                if num_edges == n - 1:
                    break

        return min_cost
