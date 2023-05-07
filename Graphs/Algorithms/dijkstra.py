# O(E logV) - listowa
# O(V^2) - macierzowa

# Graf gęsty ma E rzędu V^3
from queue import PriorityQueue

def dijkstra(G, s):
    n = len(G)
    distance = [float("inf")]*n
    visited = [False]*n
    parent = [-1]*n

    distance[s] = 0

    pq = PriorityQueue()
    pq.put((0, s))
    
    while not pq.empty():
        _, v = pq.get()
        for u, d in G[v]:
            if not visited[u] and distance[u] > distance[v] + d:
                distance[u] = distance[v] + d
                parent[u] = v
                pq.put((distance[u], u))
        visited[v] = True
    
    return parent, distance

G = [[(1, 5)], 
    [(0, 5), (2, 21), (3, 1)], 
    [(1, 21), (4, 7)], 
    [(1, 1), (4, 13), (5, 16)], 
    [(2, 7), (3, 13), (6, 4)], 
    [(3, 16), (6, 1)], 
    [(4, 4), (5, 1)]]

print(dijkstra(G, 0))