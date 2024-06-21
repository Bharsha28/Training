'''ip: l1=[6,3,2,9,4,7]
       l2=[8,7,5,3,6,9]
                
       reslut=l1(even)+l2(all odds)+l1(even)+l2(odd)+l1(even)+l2(odd)
                (6+7)+(6+5)+(6+3)+(6+9)
    op:[[13, 11, 9, 15, 9, 7, 5, 11, 11, 9, 7, 13]'''
l1=[6,3,2,9,4,7]
l2=[8,7,5,3,6,9]
def fun(l1,l2,res,i,j):
    if j==len(l2):
        j=0
        i+=1
    if i>=len(l1):
        return res
    if l1[i]%2==0:
        if l2[j]%2!=0:
            res.append(l1[i]+l2[j])
    fun(l1,l2,res,i,j+1)
    return res
print(fun(l1,l2,[],0,0))
'''ip: l1=[6,3,2,9,4,7]
       l2=[8,7,5,3,6,9]
                
       reslut=sum(l1(even)+l2(all odds)+l1(even)+l2(odd)+l1(even)+l2(odd))
                ((6+7)+(6+5)+(6+3)+(6+9))
                13, 11, 9, 15
    op:[48, 32, 40]'''
def fun(l1,l2,res,i,j,s):
    if j==len(l2):
        if s!=0:
            res.append(s)
        s=0
        j=0
        i+=1
    if i>=len(l1):
        return res
    if l1[i]%2==0:
        if l2[j]%2!=0:
            #print(l1[i],l2[j])
            s+=(l1[i]+l2[j])
    fun(l1,l2,res,i,j+1,s)
    return res
print(fun(l1,l2,[],0,0,0))