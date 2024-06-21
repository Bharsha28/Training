n=int(input())
l=list(map(int,input().split()))[:n]
l=sum(l)
n=n*((n+1)//2)
print(abs(l-n))
