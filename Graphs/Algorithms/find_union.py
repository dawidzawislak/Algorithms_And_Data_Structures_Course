n = 10

rank = [0 for _ in range(n)]
parent = [i for i in range(n)]

def Find(x):
  global parent

  if parent[x] != x:
    parent[x] =  Find(parent[x])
  
  return x


def Union(x, y):
  global rank, parent
  x_root = Find(x)
  y_root = Find(y)

  if rank[x_root] > rank[y_root]:
    parent[y_root] = x_root
  else:
    parent[x_root] = y_root
  if rank[x_root] == rank[y_root]:
      rank[y_root] += 1