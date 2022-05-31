#!/usr/bin/env python
# coding: utf-8

# In[3]:


from queue import Queue

adj_list = {
    "A" : {
        "B" : 10,
        "C" : 5
    },
    "B" : {
        "G" : 1
    },
    "C" : {
        "G" : 2
    },
    "G" : {
        
    }
}

adj_list


# In[59]:



# bfs

from collections import defaultdict

expanded = {}
parent = defaultdict(list)
cost = {}
tested_node_list = []

frontier_list = Queue()
track_fl = defaultdict(list)  #track parent node
val = 0;

#initializa

for node in adj_list.keys():
    expanded[node] = False
#     parent[node].append("")
    cost[node] = -1 #infinity
    
    
# print(expanded)
# print(parent)
# print(cost)


s = "A"
g= "G"
g_val = 0
expanded[s] = True
cost[s] = 0
frontier_list.put(val)
track_fl[val] = ["A",None,0]

while not frontier_list.empty():
    val_u = frontier_list.get()
    u = track_fl[val_u][0]
    tested_node_list.append(u)
#     print(u)
    if u == g:
        g_val = val_u
        break
    
    for v in adj_list[u].keys():
        if not expanded[v] or expanded[v]:
            expanded[v] = True
            parent[v].append(u)
#             cost[v] = cost[u] + adj_list[u][v]
            val = val + 1
            track_fl[val].append(v)
            track_fl[val].append(val_u)
#             track_fl[val].append(cost[u] + adj_list[u][v])
            frontier_list.put(val)
            
print("tested node",tested_node_list)
# print("fringe", list(frontier_list.queue))

path = []

# find goal path
while g_val != None:
    path.append(track_fl[g_val][0])
    g_val = track_fl[g_val][1]

# gp = parent[g][0]

# print(gp)

path.reverse()
print("path", "->".join(path))         #path


#path cost calulate
pathCost = 0
for i in range(0, len(path)-1):
    pathCost = pathCost + adj_list[path[i]][path[i+1]]

print("path cost",pathCost)

#frontier list
fringe = []
while not frontier_list.empty():
    val_u = frontier_list.get()
    u = track_fl[val_u][0]
    fringe.append(u)
    
print("Frontier list",fringe)
# print("path",track_fl)


# In[65]:


#take input graph, start, goal

# dfs

from collections import defaultdict

expanded = {}
cost = {}
tested_node_list = []

frontier_list = []  #initialize stack
track_fl = defaultdict(list)  #track parent node
val = 0;

#initializa

for node in adj_list.keys():
    expanded[node] = False
#     parent[node].append("")
    cost[node] = -1 #infinity
    
    
# print(expanded)
# print(parent)
# print(cost)


s = "A"
g= "G"
g_val = 0
expanded[s] = True
cost[s] = 0
frontier_list.append(val)
track_fl[val] = ["A",None,0]

while  len(frontier_list):
    val_u = frontier_list.pop()
    u = track_fl[val_u][0]
    tested_node_list.append(u)
#     print(u)
    if u == g:
        g_val = val_u
        break
    
    for v in adj_list[u].keys():
        if not expanded[v] or expanded[v]:
            expanded[v] = True
            parent[v].append(u)
#             cost[v] = cost[u] + adj_list[u][v]
            val = val + 1
            track_fl[val].append(v)
            track_fl[val].append(val_u)
#             track_fl[val].append(cost[u] + adj_list[u][v])
            frontier_list.append(val)
            
print("tested node",tested_node_list)
# print("fringe", list(frontier_list.queue))

path = []

# find goal path
while g_val != None:
    path.append(track_fl[g_val][0])
    g_val = track_fl[g_val][1]

# gp = parent[g][0]

# print(gp)

path.reverse()
print("path", "->".join(path))         #path


#path cost calulate
pathCost = 0
for i in range(0, len(path)-1):
    pathCost = pathCost + adj_list[path[i]][path[i+1]]

print("path cost",pathCost)

#frontier list
fringe = []
while  len(frontier_list):
    val_u = frontier_list.pop()
    u = track_fl[val_u][0]
    fringe.append(u)
    
print("Frontier list",fringe)
# print("path",track_fl)


# In[7]:


# ucs
from collections import defaultdict
import heapdict

expanded = {}
parent = defaultdict(list)
cost = {}
tested_node_list = []

frontier_list = heapdict.heapdict()           #returns a list
track_fl = defaultdict(list)  #track parent node
val = 0;

#initializa

for node in adj_list.keys():
    expanded[node] = False
#     parent[node].append("")
    cost[node] = -1 #infinity
    
    
# print(expanded)
# print(parent)
# print(cost)


s = "A"
g= "G"
g_val = 0
expanded[s] = True
cost[s] = 0
# frontier_list.put(val)

frontier_list[val] = 0

track_fl[val] = ["A",None,0]

while frontier_list:
    val_u = list(frontier_list.popitem())
    u = track_fl[val_u[0]][0]
    tested_node_list.append(u)
#     print(u)
    if u == g:
        g_val = val_u[0]
        break
    
    for v in adj_list[u].keys():
        if not expanded[v] or expanded[v]:
            expanded[v] = True
            parent[v].append(u)
#             cost[v] = cost[u] + adj_list[u][v]
            val = val + 1
            track_fl[val].append(v)
            track_fl[val].append(val_u[0])
            track_fl[val].append(val_u[1] + adj_list[u][v])
            frontier_list[val] = val_u[1] + adj_list[u][v]
            
print("tested node",tested_node_list)
# print("fringe", list(frontier_list.queue))

path = []

# find goal path
while g_val != None:
    path.append(track_fl[g_val][0])
    g_val = track_fl[g_val][1]

# gp = parent[g][0]

# print(gp)

path.reverse()
print("path", "->".join(path))         #path


#path cost calulate
pathCost = 0
for i in range(0, len(path)-1):
    pathCost = pathCost + adj_list[path[i]][path[i+1]]

print("path cost",pathCost)

#frontier list
fringe = []
while frontier_list:
    val_u = list(frontier_list.popitem())
    u = track_fl[val_u[0]][0]
    fringe.append(u)
    
print("Frontier list",fringe)
# print("path",track_fl)


# In[18]:


# ucs

# updated

import heapdict

expanded = {}

cost = {}
tested_node_list = []

frontier_list = heapdict.heapdict()           #returns a list
track_fl = defaultdict(list)  #track parent node
val = 0;

#initializa

for node in adj_list.keys():
    expanded[node] = False

    cost[node] = -1 #infinity
        
# print(expanded)
# print(parent)
# print(cost)


s = "A"
g= "G"
g_val = 0
expanded[s] = True
cost[s] = 0
# frontier_list.put(val)

frontier_list[val] = 0

track_fl[val] = [s,None,0]

while frontier_list:
    val_u = list(frontier_list.popitem())
    u = track_fl[val_u[0]][0]
    tested_node_list.append(u)
#     print(u)
    if u == g:
        g_val = val_u
        break
    
    for v in adj_list[u].keys():
        if not expanded[v] or expanded[v]:
            expanded[v] = True
            
#             cost[v] = cost[u] + adj_list[u][v]
            val = val + 1
            track_fl[val].append(v)
            track_fl[val].append(val_u[0])
            track_fl[val].append(val_u[1] + adj_list[u][v])
            frontier_list[val] = val_u[1] + adj_list[u][v]
            
print("tested node",tested_node_list)
# print("fringe", list(frontier_list.queue))

path = []

path_cost = g_val[1]
pathFind = g_val[0]

# find goal path
while pathFind != None:
    path.append(track_fl[pathFind][0])
    pathFind = track_fl[pathFind][1]



# print(gp)

path.reverse()
print("path", "->".join(path))         #path


print("path cost",path_cost)

#frontier list
fringe = []
while frontier_list:
    val_u = list(frontier_list.popitem())
    u = track_fl[val_u[0]][0]
    fringe.append(u)
    
print("Frontier list",fringe)
# print("path",track_fl)


# In[ ]:




