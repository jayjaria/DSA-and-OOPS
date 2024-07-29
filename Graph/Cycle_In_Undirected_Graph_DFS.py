def detect_cycle(adj_list, start):
    stack = [(start,-1)]
    visited = [False]*len(adj_list)
    visited[start] = True

    while stack:
        curr, parent = stack.pop()

        for neighbour in adj_list[curr][::-1]:
            if not visited[neighbour]:
                visited[neighbour] = True
                stack.append((neighbour, curr))

            elif neighbour!=parent:
                return True
        
    return False

adj_list = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1, 4],
    4: [1, 3, 5],
    5: [4]
}

if detect_cycle(adj_list, 4):
    print("Cycle Detected")
else:
    print("No Cycle Detected")