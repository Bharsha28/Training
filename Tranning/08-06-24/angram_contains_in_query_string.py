s=input()
query=int(input())
"""ip :school
   3
   L 2--->hoolsc
   R 3--->oolsch
   L 1---> chools
   take the first letter of each rotation resluts hoc
   hoc check annagram of hoc is persent or not"""
res=""
for i in range(query):
    d,r=input().split()
    if d=='L':
        res+=s[int(r)]
    else:
        res+=s[-int(r)]
print(res)
c=1
res=list(res)
res=sorted(res)
f=1
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if res==sorted(list((s[i:j]))):
            print("true")
            f=0
            break
if f==1:
    print("False")
s="bga"
print(sorted(s))