n=int(input())
for i in range(n):
    order=input()
    s=input()
    d={}
    for i in range(len(order)):
            d[order[i]]=i+1
    print(d)
    l=[]
    res=""
    for i in range(len(s)):
        if s[i] in d:
            l.append([d[s[i]],s[i]])
    l.sort()
    print(l)
    for i in range(len(l)):
        res+=str(l[i][1])
    print(res)
"""l=[[2,'e'],[1,'k']]
l=sorted(l)
print(l)"""
        
        
    