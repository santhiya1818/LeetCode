from typing import List

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Initialize the distance matrix for 26 lowercase letters
        inf = float('inf')
        dist = [[inf] * 26 for _ in range(26)]
        
        for i in range(26):
            dist[i][i] = 0
            
        # Fill in direct transformation costs (taking the minimum if duplicates exist)
        for u_char, v_char, c in zip(original, changed, cost):
            u = ord(u_char) - ord('a')
            v = ord(v_char) - ord('a')
            dist[u][v] = min(dist[u][v], c)
            
        # Floyd-Warshall to find shortest paths between all character pairs
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] != inf and dist[k][j] != inf:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Calculate total cost to convert source to target
        total_cost = 0
        for s_char, t_char in zip(source, target):
            if s_char != t_char:
                u = ord(s_char) - ord('a')
                v = ord(t_char) - ord('a')
                if dist[u][v] == inf:
                    return -1
                total_cost += dist[u][v]
                
        return total_cost
