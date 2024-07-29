def dfs_recursive(adj_list, start, visited):
    visited[start] = True

    print(start)
    for neighbour in adj_list[start]:
        if not visited[neighbour]:
            dfs_recursive(adj_list, neighbour, visited)


adj_list = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

visited = [False]*len(adj_list)
start = 2
dfs_recursive(adj_list, start, visited)