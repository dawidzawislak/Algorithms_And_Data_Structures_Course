def dfs(G, s=0):
    n = len(G)
    processed = []
    visited = [False]*n
    t = 0

    def dfs_visit(v):
        nonlocal G, processed, visited
        visited[v] = True
        for adj in G[v]:
            if not visited[adj]:
                dfs_visit(adj)
        processed.append(v)
    
    dfs_visit(s)

    for i in range(n):
        if not visited[i]:
            dfs_visit(i)
    
    return processed[::-1]

def reverse_edges(G):
    n = len(G)
    rev = [[] for _ in range(n)]
    for i in range(n):
        for adj in G[i]:
            rev[adj].append(i)
    
    return rev

def scc(G):
    processed = dfs(G)
    G = reverse_edges(G)

    n = len(G)
    visited = [False]*n

    def dfs_visit(v, vert):
        nonlocal G, visited
        visited[v] = True
        vert.append(v)
        for adj in G[v]:
            if not visited[adj]:
                dfs_visit(adj, vert)

    scc_tab = []

    for i in processed:
        vert = []
        if not visited[i]:
            dfs_visit(i,vert)
            scc_tab.append(vert)
    
    return scc_tab

G = [[1],[2,3],[0],[4],[5],[3]]

print(scc(G))