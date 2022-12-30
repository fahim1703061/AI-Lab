from queue import PriorityQueue
q  = PriorityQueue()
dis = []
def a(graph,h,s,g):
    dis[s] = 0
    q.put((h[s],s))
    while not q.empty():
        (val,nxt) = q.get ()
        print(nxt,end= " ")
        if (nxt == g):
            return 1
        for (i,j) in graph[nxt]:
            dis[i] = dis[nxt]+j
            q.put((h[i]+dis[i],i))
    return 0
        
graph = {
    'S': [('A',1),('B',5),('C',8)], 
    'A': [('D',3),('E',7),('G',9)],
    'B': [('G',4)],
    'C': [('G',3)],
    'D': [],
    'E': [],
    'G': []
}
h = {
    'S': 8, 
    'A': 8,
    'B': 4,
    'C': 3,
    'D': 10000000,
    'E': 10000000,
    'G': 0
}
dis = {
    'S': 10000000, 
    'A': 10000000,
    'B': 10000000,
    'C': 10000000,
    'D': 10000000,
    'E': 10000000,
    'G': 10000000

}

ans = a(graph,h,'S' ,'G')
if ans == 1:
    print("\nGoal node found") ;
else:
    print("\nGoal node not found")