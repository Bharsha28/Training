s="leet**cod*e"
l=[]
for i in s:
    if i=='*':
        l.pop()
    else:
        l.append(i)
s=""
for i in l:
    s+=i
print(s)