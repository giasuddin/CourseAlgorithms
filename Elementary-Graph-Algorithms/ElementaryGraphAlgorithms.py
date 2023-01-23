import unittest

class ElementaryGraphAlgorithms(object):

    def __init__(self) -> None:
        pass

    def bfs_sp(self, graph, start, end=None):
        print("input. start = ", start, ", end = ", end)
        queue = [(start, 0, [start])] # now it's a gray node
        visited = []
        while queue:
            node, distance, path = queue.pop(0)
            if node not in visited:
                visited.append(node) # now it's a black node
                if end is not None and node == end:
                    print("\t Shortest path found = ", path, ". Distance = ", distance)
                    return path 
                else:
                    for neighbor in graph[node]:
                        new_path = path + [neighbor]
                        queue.append((neighbor, distance + 1, new_path)) # now neigbor is the new frontier of search
        if end is None:
            print("\t No end was given. So explored all vertices using BFS = ", visited)
            return visited
        else:
            print("\t No path found!")
            return None


class GraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = {}
        self.graph[1] = {2, 5}
        self.graph[2] = {1, 3, 5}
        self.graph[3] = {2, 4}
        self.graph[4] = {3, 5, 6}
        self.graph[5] = {1, 2, 4}
        self.graph[6] = {4}
        self.ega = ElementaryGraphAlgorithms()
        
    def test_bfs_correct_order(self):
         self.assertEqual(self.ega.bfs_sp(self.graph, 1),
                          [1, 2, 5, 3, 4, 6])

    def test_bfs_correct_order_difference_source(self):
         self.assertEqual(self.ega.bfs_sp(self.graph, 5),
                          [5, 1, 2, 4, 3, 6])

    def test_bfs_correct_order_difference_source2(self):
         self.assertEqual(self.ega.bfs_sp(self.graph, 2),
                          [2, 1, 3, 5, 4, 6])

    def test_bfs_correct_order_difference_source3(self):
         self.assertEqual(self.ega.bfs_sp(self.graph, 4),
                          [4, 3, 5, 6, 2, 1])

    def test_bfs_correct_order_difference_source4(self):
         self.assertEqual(self.ega.bfs_sp(self.graph, 3),
                          [3, 2, 4, 1, 5, 6])

    def test_bfs_shortest_path(self):
         self.assertEqual(self.ega.bfs_sp(self.graph, 1, 6),
                          [1, 5, 4, 6])
    def test_bfs_shortest_path_2(self):
         self.assertEqual(self.ega.bfs_sp(self.graph, 5, 6),
                          [5, 4, 6])    
    
    def test_bfs_shortest_path_3(self):
         self.assertEqual(self.ega.bfs_sp(self.graph, 1, 7),
                          None)

    # def test_bfs_shortest_path_4(self):
    #      self.assertEqual(self.ega.bfs_sp(self.graph, 1, 4),
    #                       [1,2,3,4]) # this should fail
if __name__ == "__main__":
    unittest.main()


