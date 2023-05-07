# G - skierowany
# O(VE)
def bellman_ford(G, s):
    n = len(G)
    distance = [float("inf")]*n
    parent = [-1]*n

    distance[s] = 0

    # Relaksacje
    for v in range(n):
        for (u, d) in G[v]:
            if distance[u] > distance[v] + d:
                distance[u] = distance[v] + d
                parent[u] = v
    
    # Weryfikacja(wykrywanie ujemnych cykli)
    for v in range(n):
        for (u, d) in G[v]:
            if distance[u] > distance[v] + d:
                return None
    
    return parent, distance


G = [[(1, 3)],
     [(2, 1)],
     [(3, 2)],
     [(1, -4), (4, 2)],
     []]

print(bellman_ford(G, 0))