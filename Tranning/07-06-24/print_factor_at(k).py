n=int(input())
k=int(input())
def factors(n,i,c,k):
    if i==0:
        return 
    if n%i==0:
        c+=1
    if k==c:
        return i
    return factors(n,i-1,c,k)
i=n
print(factors(n,i,0,k))