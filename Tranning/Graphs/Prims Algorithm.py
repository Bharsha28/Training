g={1:[(2,2),(1,5)],2:[(2,1),(2,3)],5:[(1,1),(1,4)],4:[(1,5),(3,3)],3:[(2,2),(3,4)]}
def prims(d):
    visited=[]
    queue=[(0,d)]
    c=0
    while queue:
        queue.sort()
        ele=queue.pop(0)
        c,val=ele8
        c+=c
        if val in visited:
             continue
        visited.append(val)
        for i in g[val]:
            if i[1] not in visited and i[1] not in queue:
                queue.append(i)
    return c,visited
print(prims(1))