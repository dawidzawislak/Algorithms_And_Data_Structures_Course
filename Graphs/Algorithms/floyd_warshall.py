# O(V^3)
# Ścieżki między każdą parą wierzchołków
# G dane jako macierz sąsiedztwa

def floyd_warshall(G):
  inf = float("inf")
  n = len(G)
  distance = [[inf for _ in range(n)] for _ in range(n)]
  parent = [[None for _ in range(n)] for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if G[i][j]  != 0:
        distance[i][j] = G[i][j]
    distance[i][i] = 0
    parent[i][i] = i

  for t in range(n):
    for x in range(n):
      for y in range(n):
        d1 = distance[x][y]
        d2 = distance[x][t] + distance[t][y]
        if d1 > d2:
          distance[x][y] = d2
          parent[x][y] = parent[t][y]
  
  for i in range(n):
    if distance[i][i] < 0:
      return False
  
  return distance, parent