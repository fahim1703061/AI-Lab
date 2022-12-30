
def ids(graph, s, g):
    q = [] 
    t = [] 
    z = []
    q.append(s)
    while q:
        now = q.pop(0)
        print(now)
        z.append(now)
        for i in graph[now]:
            print(i)
            t.append(i)
            if (i == g):
                return 1
        if not q:
            while z:
                now = z.pop(0)
                print(now)
            q = t
            t = []

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

ans = ids(graph,'S' ,'G')
if ans == 1:
    print("\nGoal node found") ;
else:
    print("\nGoal node not found")