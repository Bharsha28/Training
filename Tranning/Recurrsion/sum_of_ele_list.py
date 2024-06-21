"sumof list without using sum variable"
l=[1,2,3,4,5]
def sum1(n):
    if n==len(l):
        return 0
    print(n)
    t=l[n]+sum1(n+1)
    print(" ",n)
    return 0
print(sum1(0))