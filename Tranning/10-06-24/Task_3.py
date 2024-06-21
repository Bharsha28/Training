"""4
tued
fwow
rore
drui
word
No"""
n=int(input())
l=[]
for i in range(n):
    l.append(input())
tar=input()
def count(i,j,k,t):
    if k==len(tar) and t==1:
        return 1
    if i>=n or j>=n or i<0 or j<0 or l[i][j]!=tar[k] :
        return 
    if l[i][j] in tar[k]:
        l[i][j]='0'
    if t==0:
        t=count(i-1,j,k+1,t)
        t=count(i+1,j,k+1,t)
        t=count(i,j-1,k+1,t)
        t=count(i,j+1,k+1,t)
    return t
for i in range(n):
    for j in range(n):
        if l[i][j]==tar[0]:
            c=count(i,j,1,0)
            if c==1:
                print("Yes")
                break
else:
    print("no")
