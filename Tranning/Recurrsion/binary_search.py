"binary search using recurssion"
l=[1,2,3]
key=1
def binary(low,high,key):
    if low>high:
        return [0,""]
    mid=(low+high)//2
    if l[mid]==key:
        return [1,mid]
    elif l[mid]<key:
         return binary(mid+1,high,key)
    else:
        return binary(low,mid-1,key)
n=len(l)
t=binary(0,len(l),key)
if t[0]==False:
    print("Not found",t[1])
else:
    print("Found at ",t[1])