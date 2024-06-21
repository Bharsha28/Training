g={5:[3,7],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
def dfs(d,l):
     l.append(d)
     for i in g[d]:
         if i not in l:
             dfs(i,l)
     return l
print(dfs(5,[]))
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
allpaths(5,[],2)

