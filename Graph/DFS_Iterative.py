def dfs_iterative(adj_list, start):
    stack = [start]
    visited = [False]*len(adj_list)
    visited[start] = True

    while stack:
        node = stack.pop()
        print(node)

        for neighbour in adj_list[node][::-1]:
            if not visited[neighbour]:
                stack.append(neighbour)
                visited[neighbour] = True


adj_list = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

start = 0

dfs_iterative(adj_list, start)