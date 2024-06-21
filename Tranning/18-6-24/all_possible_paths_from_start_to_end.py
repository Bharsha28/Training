n=int(input())
m=int(input())
l=[[0 for i in range(n)]for j in range(m)]
def fun1(i,j,l,c):
    if i<0 or j>=m or i>=n or j<0:
        return c
    if i==n-1 and j==m-1:
        c+=1
        return c
    l.append((i,j))
    if (i-1,j) not in l:
        c=fun1(i-1,j,l,c)
    if (i,j-1) not in l:
        c=fun1(i,j-1,l,c)
    if (i+1,j) not in l:
        c=fun1(i+1,j,l,c)
    if (i,j+1) not in l:
        c=fun1(i,j+1,l,c)
    print(l)
    l.pop()
    return c
print(fun1(0,0,[],0))

