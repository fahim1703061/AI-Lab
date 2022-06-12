#define graph with adjacent list
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
visited = {} #Stack for visited nodes
print(sample_graph)

def dfs_traversal(graph1,node,visited):
     if node not in visited:
         visited.append(node)
         for i in sample_graph[node]:
            dfs_traversal(sample_graph,i,visited)
     return visited

visited  = dfs_traversal(sample_graph,'A',[])
print("Stack: ",visited)
