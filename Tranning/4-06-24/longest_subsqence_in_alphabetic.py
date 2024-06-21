n=input()
val=ord(n[0])
max1=1
c=1
for i in range(1,len(n)):
    val+=1
    if val==ord(n[i]):
        c+=1
        val=ord(n[i])
    else:
        c=1
        val=ord(n[i])
    max1=max(max1,c)
print(max1)
    
    