from collections import deque

def detect_cycle_bfs(adj_list, start):
    queue = deque([(start, -1)])
    visited = [False]*len(adj_list)
    visited[start] = True

    while queue:
        curr, parent = queue.popleft()

        for neighbour in adj_list[curr]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append((neighbour, parent))
                
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

if detect_cycle_bfs(adj_list, 0):
    print("Cycle Detected")
else:
    print("No Cycle Detected")
    
    



    