l=[3,2,5,4,1,6,8]
'''l1=[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
                    l1.append([l[i],l[j],l[k]])
print(l1)'''
'''def kcom(l,i,j,k,l2):
    if i==len(l)-1:
        return
    else:
        if k==len(l):
            kcom(l,i,j+1,j+2,l2)
        elif j==len(l):
            kcom(l,i+1,i+2,i+3,l2)
        else:
            l2.append([l[i],l[j],l[k]])
            kcom(l,i,j,k+1,l2)
    return l2
print(kcom(l,0,1,2,[]))'''
def kcom(l,i,j,k,t,l2):
    print(i,j,k,l2)
    if i==len(l)-1:
        return
    else:
        diff=abs(k-t)
        if k==diff:
            kcom(l,i,j,j+diff,t+1,l2)
        if diff==len(l):
            kcom(l,i,j+1,j+diff,t,l2)
        elif j==len(l):
            kcom(l,i+1,i+2,i+diff,t+1,l2)
        else:
            l2.append([l[i],l[j],l[k:t]])
            kcom(l,i,j,k+diff,t,l2)
    return l2
l2=[]
t=4
print(kcom(l,0,1,2,t,l2))
            
        
