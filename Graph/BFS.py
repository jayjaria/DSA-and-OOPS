from collections import deque

def bfs(adj_list, start):
    visited = [False]*len(adj_list)
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node)

        for neighbour in adj_list[node]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour]=True



adj_list = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1, 5],
    5: [2, 4]
}

start = 0
bfs(adj_list, start)