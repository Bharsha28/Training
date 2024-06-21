'''printing all path from 5 to all nodes'''
g={5:[3,7],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
def allpaths(d,l,end):
     l.append(d)
     if d==end:
         print(l)
         l.pop()
         return
     for i in g[d]:
         if i not in l:
             allpaths(i,l,end)
     l.pop()
print("All paths from start to end")
for i in g:
    if i!=5:
        print("path from 5 to ",i)
        allpaths(5,[],i)