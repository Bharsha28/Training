# t=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
# m=[5,6,5,4,11,2]
# i=0
# max1=0
# for i in range(len(t)):
#     curr=m[i]
#     k=t[i][1]
#     for j in range(i+1,len(t)):            
#         if t[j][0]>=k and t[i][1]<=t[j][0]:
#             ls=t[j][1]
#             #print(t[i],t[j],curr,max1)
#             curr+=m[j]
#             #print(m[i],m[j])
#         elif k==t[j][0]:
#             curr=0
#             curr=m[i]
#             curr+=m[j]
#             #print(curr)
#             max1=max(curr,max1)
#             continue
#         max1=max(curr,max1)
# print(max1)
t=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
b=a.copy()
for i in range(1,len(t)):
    for j in range(0,i):            
        if t[j][1]<=t[i][0]:
            if (b[j]+a[i])>=b[i]:
              b[i]=a[i]+b[j]
            
print(max(b))