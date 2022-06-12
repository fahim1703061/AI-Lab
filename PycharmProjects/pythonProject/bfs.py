from queue import Queue
#define graph with adjacent list
from typing import Dict, Any

sample_graph = {
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
visited: dict[Any, Any] = {} #Stack for visited nodes
print(sample_graph)

def bfs_traversal(graph,root,goal):
    queue = [root] #Q='A'

    while queue:
        node=queue.pop()
        if node not in visited:
            visited.add(node)

            if node==goal:
                return
            for neighbor in sample_graph[node]:
                if neighbor not in visited:
                    queue.appendleft(neighbor)
    return visited

visited = bfs_traversal(sample_graph,'A',[])
print("Stack: ",visited)