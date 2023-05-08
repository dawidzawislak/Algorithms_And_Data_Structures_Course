def find_bridges(G):
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    d = [-1]*n
    low = [None]*n

    time = 1

    bridges = []

    def dfs_visit(v):
        nonlocal G, visited, d, parent, low, time
        visited[v] = True
        d[v] = time
        low[v] = time
        time += 1

        for adj in G[v]:
            if not visited[adj]:
                parent[adj] = v
                dfs_visit(adj)

        for adj in G[v]:
            if parent[v] == adj:        
                low[adj] = min(low[adj], low[v])
            else:
                low[v] = min(d[adj], low[v])


    for i in range(n):
        if not visited[i]:
            dfs_visit(i)
    
    for v in range(n):
            if low[v] == d[v] and parent[v] != None:
                bridges.append((parent[v], v))
    

    return bridges

G = [[1,2],
     [0,2,6],
     [0,1,3],
     [2,4,5],
     [3,5],
     [3,4],
     [6]]

print(find_bridges(G))