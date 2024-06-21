'''
ip:3
    1 0 1
    0 0 1
    0 1 1
    row,col=2,2
output: 1(here 2,2 is 1 where 1 represent tree and 0 repersent not a tree if given row and col is 1 then it's up or down or rigth or left fire occures and return no.of tree which is not affected by fire'''

n=int(input())
l=[]
for i in range(n):
    l1=[]
    for j in range(n):
        l1.append(int(input()))
    l.append(l1)
def count(r,c,m):
        #print(l,r,c)
        if c>=n or r>=n or r<0 or c<0 or l[r][c]!=1:
            return m
        if l[r][c]==1:
            m+=1
            l[r][c]=2
            m=count(r-1,c,m)
            m=count(r+1,c,m)
            m=count(r,c-1,m)
            m=count(r,c+1,m)
        return m
        
cou=0
maz=0
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            cou+=1
            p=count(i,j,0)
            maz=max(p,maz)
        
print(cou)
print("max",maz)
n=int(input())
print(n//360,":y",(n//360)%30,":m",((n//360)%30)%6,":w",((n//360)%30)/6,":d")

