#define graph
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
visited = {} #Stack for visited nodes
print(graph)

def dfs_traversal(graph1,node,visited):
     if node not in visited:
         visited.append(node)
         for i in graph[node]:
            dfs_traversal(graph,i,visited)
     return visited

visited  = dfs_traversal(graph,'A',[])
print("Stack: ",visited)
