from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for a, b, distance in roads:
            graph[a].append((b, distance))
            graph[b].append((a, distance))
        
        queue = deque([(1, float('inf'))])  # Tupla (cidade, escore mínimo)
        
        min_scores = {1: float('inf')}
        
        while queue:
            city, min_score = queue.popleft()
            
            if min_score > min_scores[city]:
                continue
            
            for neighbor, distance in graph[city]:
                neighbor_min_score = min(min_score, distance)
                
                if neighbor_min_score < min_scores.get(neighbor, float('inf')):
                    min_scores[neighbor] = neighbor_min_score
                    queue.append((neighbor, neighbor_min_score))
        
        return min_scores[n]
