"""
using recursion print sum of even numbers with two lists
ip:
    a=[3,8,5,4,3]
    b=[5,0,9,3,2]
op:
    (a list even sum, b list odd sum)
"""
def add(i1,i2,es,os):
    if i1>=len(l1) and i2>=len(l2):
        return (es,os)
    if l1[i1]%2==0:
        es+=l1[i1]
    if l2[i2]%2!=0:
        os+=l2[i2]
    return add(i1+1,i2+1,es,os)
l1=[3,8,5,4,3]
l2=[5,0,9,3,2]
print(add(0,0,0,0))
'''def add(i1,i2,es,os):
    def leftelel1(i1,es):
        if l1[i1]%2==0:
        es+=l1[i1]
    def leftelel1(i1,i2,es,os):
        if l2[i2]%2!=0:
        os+=l2[i2]
    if i1==len(l1) and i2==len(l2):
        return (es,os)
    else:
        leftelel1(i1,es)
    if l1[i1]%2==0:
        es+=l1[i1]
    if l2[i2]%2!=0:
        os+=l2[i2]
    return add(i1+1,i2+1,es,os)
l1=[1,2,3,4]
l2=[5,6,7,8,1]
print(add(0,0,0,0))'''