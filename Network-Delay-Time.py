import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for u, v, w in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((v, w))
        
        dist = {node: float('inf') for node in range(1, n+1)}
        dist[k] = 0
        
        pq = [(0, k)]
        
        while pq:
            curr_dist, node = heapq.heappop(pq)
            
            if curr_dist > dist[node]:
                continue
            
            if node in graph:
                for neighbor, travel_time in graph[node]:
                    total_dist = curr_dist + travel_time
                    
                    if total_dist < dist[neighbor]:
                        dist[neighbor] = total_dist
                        heapq.heappush(pq, (total_dist, neighbor))
        
        max_dist = max(dist.values())
        if max_dist == float('inf'):
            return -1
        
        return max_dist
