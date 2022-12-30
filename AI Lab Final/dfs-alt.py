def dfs(graph, s, g):
    print(s , end =" ")
    if (s == g) :
        return 1
    ans = 0 
    for i in graph[s]:
        if dfs(graph,i,g):
            return 1
    return ans 


graph = {
    'S' : ['A','B','C'] ,
    'A' : ['D' , 'E'] ,
    'B' : ['G'] ,
    'C' : ['F'] ,
    'D' : ['H'] ,
    'E' : ['G'] ,
    'G' : [] ,
    'F' : ['G'],
    'H' : []         
}

ans = dfs(graph,'S' ,'G')
if ans == 1:
    print("\nGoal node found") ;
else:
    print("\nGoal node not found")