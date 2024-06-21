#d={5:[(7,2),(3,1)],7:[(5,2),(4,3),(3,4)],4:[(7,3),(8,2),(2,6)],8:[(2,4),(3,1),(4,2)],3:[(5,2),(7,4),(8,1)],2:[(4,6),(8,4)]}
d={2:[(5,2),(3,1)],3:[(2,1),(5,2),(7,3),(8,3)],4:[(9,2),],5:[(2,2),(3,2),(8,2)],6:[(8,4),(9,2)],7:[(3,3),(9,1)],8:[(5,2),(3,3),(6,4)],9:[(6,2),(7,1),(4,2)]}
def fuc(k,v,q,l,pc):
    v[k]=1
    pc[k]=0
    q.append(k)
    while(len(q)!=0):
        min1=999
        for i in q:
            if min1>pc[i]:
                min1=pc[i]
                ind=i
        k=ind
        if k not in l:
            l.append(k)
        v[k]=1
        for i in d[k]:
             if not v[i[0]]:
                 q.append(i[0])
                 if pc[i[0]]>pc[k]+i[1]:
                      pc[i[0]]=pc[k]+i[1]
        q.pop(0)
    c=pc.count(99999)
    for i in range(c):
        pc.remove(99999)
    return l,pc
               
v=[0]*10
pc=[99999]*10 
v,c=fuc(5,v,[],[],pc)
print(v,c)
print(list(zip(v,c)))