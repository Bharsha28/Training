"""
return sum of all even numbers from 1 to n using recursion
"""
def add(x,s):
    if x>n:
        return s
    if x%2==0:
        s+=x
    return add(x+2,s)
n=4
print(add(2,0))
def add1(x):
    if x==0:
        return 0
    return x+add1(x-2)
n=11
if n%2==0:
    print(add1(n))
else:
    print(add1(n-1))
'''n=int(input())
def even_sum(n,i,s):
    if i>n:
        return s
    if i%2==0:
        s+=i
    return even_sum(n,i+2,s)

flag=False
if n<0:
    n=n*-1
    flag=True
if flag==True:
    print((even_sum(n,2,0))*-1)
else:
    print(even_sum(n,2,0))'''