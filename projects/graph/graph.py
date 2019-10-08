"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.dft_visited = set()
        self.dfs_visited = set()

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v2 in self.vertices and v1 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("edge can not created from v1 and v2")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()
        visited = set()

        queue.enqueue(starting_vertex)
        while queue.size() > 0:
            vertex = queue.dequeue()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vertex in self.vertices[vertex]:
                    queue.enqueue(next_vertex)



    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()

        stack.push(starting_vertex)
        while stack.size() > 0:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                for next_vertex in self.vertices[vertex]:
                    stack.push(next_vertex)

 
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        print (starting_vertex)
        self.dft_visited.add(starting_vertex)


        adjacent_vertices = self.vertices[starting_vertex]
        if adjacent_vertices:
            for adjacent_vertex in adjacent_vertices:
                if adjacent_vertex not in self.dft_visited:
                    self.dft_recursive(adjacent_vertex)

    
    # #################### Solution code ##########################
    
    # def dft_recursive(self, starting_vertex, visited=None):

    #     if visited is None:
    #         visited = set()
        
    #     print(starting_vertex)
    #     visited.add(starting_vertex)
    #     for child_vertex in self.vertices[starting_vertex]:
    #         if child_vertex not in visited:
    #             self.dft_recursive(child_vertex, visited)


    ##########################################################



        



    def bfs(self, starting_vertex, destination_vertex):

        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # start is destitnation? done!
        if starting_vertex == destination_vertex:
            return [starting_vertex]

        else:

            #will contain complete paths
            queue = Queue()
            queue.enqueue([starting_vertex])

            visited = set()


            while queue:

                path = queue.dequeue()
                last_vertex = path[-1]

                adjacent_vertices = self.vertices[last_vertex]

                # cycle through all non visited adjacent vertices
                for adjacent_vertex in adjacent_vertices:
                    if adjacent_vertex not in visited:
                        new_path = path.copy()
                        new_path.append(adjacent_vertex)
                        if adjacent_vertex == destination_vertex:
                            return new_path
                        else:
                            queue.enqueue(new_path)
                visited.add(last_vertex)
                
                
            return []


    # #################### Solution code ##########################

    # def bfs(self, starting_vertex, destination_vertex):
        
    #     qq = Queue()
    #     visited = set()
    #     qq.enqueue([starting_vertex])

    #     while qq.size() > 0:
    #         path = qq.dequeue()
    #         vertex = path[-1]
    #         if vertex not in visited:
    #             if vertex == destination_vertex:
    #                 return path
    #             visited.add(vertex)

    #             for next_vert in self.vertices[vertex]:
    #                 new_path = list(path) #deep copy !
    #                 new_path.append(next_vert)
    #                 qq.enqueue(new_path)
        # #########################################################
            
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        start_path = [starting_vertex]

        if starting_vertex == destination_vertex:
            return [starting_vertex]

        else:
            # Flag current vertex as visited
            self.dfs_visited.add(starting_vertex)

            # get set of adjacent vertices
            adjacent_vertices = self.vertices[starting_vertex]

            # get adjacent vertices not already visited
            adjacent_not_visited = adjacent_vertices.difference(
                self.dfs_visited)

            #process adjacent vertices not already visited
            for adjacent_vertex in adjacent_not_visited:
                found = self.dfs(adjacent_vertex, destination_vertex)
                if found:
                    return start_path + found
            return None

    
    
    # #################### Solution code ##########################
                
    # def dfs(self, starting_vertex, destination_vertex):
                      

    #     s = Stack()
    #     visited = set()
    #     s.push([starting_vertex])

    #     while s.size() > 0:
    #         path = s.pop()
    #         vertex = path[-1]
    #         if vertex not in visited:
    #             if vertex == destination_vertex:
    #                 return path
    #             visited.add(vertex)

    #             for next_vert in self.vertices[vertex]:
    #                 new_path = list(path) #deep copy !
    #                 new_path.append(next_vert)
    #                 s.push(new_path)

        # #########################################################






if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("dft(1): ")
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print("bft(1)")
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print("dft_recursive(1):")
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print("bfs(1, 6)")
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("dfs(1, 6)")
    print(graph.dfs(1, 6))
