from queue import PriorityQueue
graph = {
    'A':['B','E'],
    'B':['F','D'],
    'E':['G','C'],
    'D':['B'],
    'E':['A','C','G'],
    'F':['B'],
    'G':['E'],
    'C':['E','K'],
    'K':['C','H','I'],
    'H':['K'],
    'I':['K']
}
class graph_class:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def neighbors(self, node):
        return self.edges[node]

    def get_cost(self,starting_node, destination_node):
        return self.weights[(starting_node+destination_node)]


def uniform_search(graph, start, goal):
    visited = {}
    queue = PriorityQueue()
    queue.put((start,0))

    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.add(node)

            if node == goal:
                return
            for i in graph.neighbors(node):
                if i not in visited:
                    total_cost = cost + graph.get_cost(node, i)
                    queue.put((total_cost,i))
                    print("cost:", total_cost)
                return total_cost

