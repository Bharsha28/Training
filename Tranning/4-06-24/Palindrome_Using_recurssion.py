def palind(n,s):
    if n<=0:
        return s
    r=n%10
    s=(s*10)+r
    return palind(n//10,s)
    
n=int(input())
s=0
res=palind(n,s)
if n==res:
    print("palindrome")
else:
    print("not")