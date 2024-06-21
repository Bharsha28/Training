queue=[]
def bfsOfGraph( V ,adj ):
    queue=[0]
    visited=[]
    while queue:
        ele=queue.pop(0)
        #print(ele,end=" ")
        visited.append(ele)
        print(visited,end=" ")
        for i in range(len(adj[0])):
            if adj[i] not in visited and adj[i] not in queue:
                queue.extend(adj[i])
    return visited
V = 5
E = 4
adj = [[1,2,3],[],[4],[],[]]
print(len(adj))
print(bfsOfGraph(V,adj))
