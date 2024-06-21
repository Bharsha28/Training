l=list(map(int,input().split()))
i=0
j=2
while(j<=len(l)):
    print(i,j)
    if l[i]>l[i+1]:
        l[i],l[i+1]=l[i+1],l[i]
    if l[i]>l[j-1]:
        l[i],l[j-1]=l[j-1],l[i]
    if l[i+1]>l[j-1]:
        l[i+1],l[j-1]=l[j-1],l[i+1]
    i+=1
    j+=2
print(l)
'''k=3
def sorts(j):
    i=j
    for  i in range(k):
        for j in range(i+1,k):
            if l[j-1]>l[j]:
                l[j-1],l[j]=l[j],l[j-1]
for i in range(len(l)):
    sorts(i)
print(l)'''