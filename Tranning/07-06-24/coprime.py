import math
n=int(input())
m=int(input())
c=0
for i in range(2,(min(n,m)//2)+1):
    if n%i==0 and m%i==0:
        c+=1
if c==0:
    print("co prime")
else:
    print("not")
