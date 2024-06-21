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
    for j in range(1,mon+1):
           if l[i-1][j]==1:
               l[i][j]=1
           else:
               if j<c[i]:
                   l[i][j]=l[i-1][j-1]
               elif c[i]==j:
                    l[i][j]=1

               else:
                   m=j-c[i]
                   if m<0:
                       l[i][j]=0
                   else:
                       ele=l[i-1][m]
                       l[i][j]=ele
print(l)               
if l[-1][-1]==1:
    print("Yes")
else:
    print("No")
            
               
    
