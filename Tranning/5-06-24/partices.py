def fun(x):
    if x==3:
        return 500
    print(x)
    t=fun(x+1)
    print(x)
    return t
print(fun(1))
def printGfg(n):
        # Code here
        if n==0:
            return 0
        print("GFG ",end=" ")
        return printGfg(n-1)
print(printGfg(5))
def printNos(N):
        #Your code here
    if N==0:
        return 
    printNos(N-1)
    print(N,end=" ")
printNos(10)
#"Factorial"
N=6
l=[]
for i in range(1,N):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    if fact<=N:
      l.append(fact)
print(l)
        


