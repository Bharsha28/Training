g={5:[(3,1),(7,2)],7:[(5,2),(4,3),(3,4)],4:[(7,3),(8,2),(2,6)],8:[(3,1),(4,2),(2,4)],3:[(5,1),(7,4),(8,1)],2:[(4,6),(8,4)]}
# def cost(d,l,s,min1):
#      l.append(d)
#      for i in g[d]:
#          if i[0] not in l:
#              s+=i[1]
#              min1=min(min1,s)
#              #print(min1)min1)
#      return (l,min1)
# #print(cost(5,[],0,100))
def allpaths(d,l,end,s,min1,l1):
     l.append(d)
     if d==end:
         if (s<min1):
             min1=s
             l1=l.copy()
         min1=min(min1,s)
         e=l.pop()
         return (l1,min1)
     for i in g[d]:
         if i[0] not in l:
             s+=i[1]
             l1,min1=allpaths(i[0],l,end,s,min1,l1)
             s-=i[1]
     l.pop()
     return (l1,min1)
print(allpaths(5,[],2,0,100,[]))
