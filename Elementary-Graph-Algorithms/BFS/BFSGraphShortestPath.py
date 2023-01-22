def bfs_sp(graph, start, goal=None):
    explored = []
    
    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]
    
    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return
    
    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
            
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                
                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)

    # Condition when the nodes
    # are not connected
    if goal is None:
        print("all explored =", explored)
    else:
        print("So sorry, but a connecting"\
                    "path doesn't exist :(")
    
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


