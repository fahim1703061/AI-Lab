from queue import PriorityQueue
q  = PriorityQueue()
def bfs(graph, s, g):
    q.put(s)
    print("Expanded nodes: " , end =" ")
    while not q.empty():
        now = q.get()
        print(now,end= " ")
        if now == g:
            return 1
        for i in graph[now]:
            q.put(i)


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

ans = bfs(graph,'S' ,'G')
if ans == 1:
    print("\nGoal node found") 
else:
    print("\nGoal node not found")