l=list(map(int,input().split()))
s=0
max1=0
for i in range(1,len(l)):
    p=l[i-1]
    q=l[i]
    for j in range(q-1,p,-1):
        c=1
        for k in range(2,(j//2)+1):
            if j%k==0:
                c=0
                break
        if c==1:
            max1=max(max1,j)
    s+=max1
print(s)

        
        
