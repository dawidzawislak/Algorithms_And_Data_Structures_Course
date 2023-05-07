def dfs(G):
    n = len(G)
    visited = [False]*n
    counter = 0

    def dfsVisit(i):
        nonlocal G, visited

        visited[i] = True
        for adj in G[i]:
            if visited[adj] == False:
                dfsVisit(adj)

    for i in range(n):
        if visited[i] == False:
            dfsVisit(i)
            counter += 1
            