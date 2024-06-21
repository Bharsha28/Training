"""
ip:-
    list with some numbers, those are the quantities of gold available in that house. A theif is planning to steel. If he steels in one house he won't steel exact next house. Find how much max gold can he steel.
    [13,9,4,10,5,7]
op:-
    30
"""
l=[13,9,4,10,5]

def rec_fun(i,x):
    if i>=x:
        return 0
    mx=0
    for j in range(i,x):
        s=l[j]
        s+=rec_fun(j+2,x)
        if mx<s:
            mx=s
    return mx

print(rec_fun(0,len(l)))


    
        
"""def alter(j,x):
    sum1=0
    for i in range(j,x,2):
        sum1+=(l[i])
    return sum1
max1=0
for i in range(len(l)):
    s=alter(i,len(l))
    s+=l[i]
    print(s)
    max1=max(max1,s)
print(max1)"""
        