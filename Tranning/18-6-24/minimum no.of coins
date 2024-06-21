c=list(map(int,input().split()))
c.sort()
mon=int(input())
l=[]
m=mon+1
for i in range(len(c)):
    l1=[0]*m
    l.append(l1)
k=0
for i in range(len(c)):
    for j in range(mon+1):
            m=abs(c[i]-j)
            if m<0:
                l[i][j]=0
            if m==0:
                l[i][j]=1
            else:
                ele=l[i][m]
                l[i][j]=ele+1
print(l)
min1=99
for i in range(len(c)):
    min1=min(min1,l[i][mon])
print(min1)
    