'''
ip:3
    1 0 1
    0 0 1
    0 1 1
    row,col=2,2
output: 1(here 2,2 is 1 where 1 represent tree and 0 repersent not a tree if given row and col is 1 then it's up or down or rigth or left fire occures and return no.of tree which is not affected by fire'''
n=int(input())
row=int(input())
col=int(input())
l=[]
for i in range(n):
    l1=[]
    for j in range(n):
        l1.append(int(input()))
    l.append(l1)
c=0
if l[row][col]==0:
    for i in range(n):
        for j in range(n):
            if l[i][j]==1:
                c+=1
    print(c)
else:
    c=0
    def count(r,c):
            #print(l,r,c)
            if c>=n or r>=n or r<0 or c<0 or l[r][c]==2:
                return 0
            if l[r][c]==0:
                return 0
            if l[r][c]==1:
                l[r][c]=2
                count(r-1,c)
                count(r+1,c)
                count(r,c-1)
                count(r,c+1)
            return count(r,c)
    count(row,col)
    for i in range(n):
        for j in range(n):
            if l[i][j]==1:
                c+=1
    print(c)

    
    