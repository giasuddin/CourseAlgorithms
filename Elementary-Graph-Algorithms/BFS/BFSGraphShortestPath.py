def bfs_sp(graph, start, end=None):
    queue = [(start, 0, [start])]
    visited = []
    while queue:
        node, distance, path = queue.pop(0)
        if node not in visited:
            visited.append(node)
            if end is not None and node == end:
                print("Shortest path found = ", path, ". Distance = ", distance)
                return 
            else:
                for neighbor in graph[node]:
                    new_path = path + [neighbor]
                    queue.append((neighbor, distance + 1, new_path))
    if end is None:
        print("No end was given. So explored all vertices using BFS = ", visited)
    else:
        print("No path found!")
    return
# Driver Code
#if __name__ == "__main__":
graph = {}
graph[1] = {2, 5}
graph[2] = {1, 3, 5}
graph[3] = {2, 4}
graph[4] = {3, 5, 6}
graph[5] = {1, 2, 4}
graph[6] = {4}
    
bfs_sp(graph, 1, 6)
bfs_sp(graph, 1)
bfs_sp(graph, 5)
bfs_sp(graph, 1, 7)


