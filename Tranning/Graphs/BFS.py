graph={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2,12],3:[5,7,8],2:[4,8,9],9:[2],12:[8],13:[]}
queue=[]
def bfs(k):
    visited=[]
    queue=[k]
    while queue:
       ele=queue.pop(0)
       print(ele,end=" ")
       visited.append(ele)
       for i in graph[ele]:
           if i not in visited and i not in queue:
               #visited.append(i)
               queue.append(i)
    return visited
bfs(5)
print()
#bfs(3)
"""or"""
'''def bfs(k):
    visited=[k]
    queue=[k]
    while queue:
       ele=queue.pop(0)
       print(ele,end=" ")
       for i in graph[ele]:
           if i not in visited:
               visited.append(i)
               queue.append(i)
bfs(5)
print()'''
    