s=input()
l=[]
for i in range(len(s)):
    for j in range(i+1,len(s)):
        l.append(s[i:j+1])
max1=0
print(l)
for i in range(len(l)):
    s=l[i]
    if s==s[::-1]:
        max1=max(max1,len(l[i]))
if max1!=0:
    print(max1)
else:
    print(-1)