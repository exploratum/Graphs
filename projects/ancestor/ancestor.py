

# class Graph:
#         def __init__(self):
#             self.vertices = {}

#         def add_vertex(self, vertex_id):
#             if vertex_id not in self.vertices:
#                 self.vertices[vertex_id] = set()

#         def add_edges(self, v1, v2):
#             if v1 in self.vertices and v2 in self.vertices:
#                 self.vertices[v1].add(v2)
#             else:
#                 raise IndexError("That vertex does not exist")

def earliest_ancestor(ancestors, child):


    if not find_parents(ancestors, child):
        return -1

    qq = Queue()
    qq.enqueue([child])
    solutions = []

    while qq:
        parents = qq.dequeue()
        older_parents = []

        for parent in parents:
            older_parents.extend(find_parents(ancestors, parent))
        
        if older_parents: 
            qq.enqueue(older_parents)
        else:
            solutions.extend(parents)
            break

    if solutions:
        return min(solutions)
    else:
        return -1 


# Find direct parents of a child
def find_parents(ancestors, child):
    parents = []
    for node in ancestors:
        if node[1] == child:
            parents.append(node[0])

    return parents



class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
    
    