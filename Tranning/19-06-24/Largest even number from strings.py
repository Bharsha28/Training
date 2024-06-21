'''tu5g2k1h8
g5g8gd6h3'''
s1=input()
s2=input()
l=[]
for i in s1:
    if not i.isalpha() and int(i) not in l:
        l.append(int(i))
for i in s2:
    if not i.isalpha() and int(i) not in l:
        l.append(int(i))
l.sort(reverse=True)
'''print(l)
i=len(l)-3
j=len(l)-1
while(i>0):
    if l[i]%2==0:
        l[i],l[j]=l[j],l[i]
    i-=1  
# for i in range(len(l)-1,0,-1):
#     if l[i]%2!=0:
#         l[i],l[i-1]=l[i-1],l[i]
l="".join(str(l))
print(l)'''
s3=""
min1=9999
for i in range(len(l)):
    if l[i]%2==0:
        if l[i]<min1:
            min1=l[i]
if min1==9999:
    print("Not possible")
else:
    l.remove(min1)
    print(l)
    for i in l:
        s3=s3+str(i)
    print(s3+str(min1))
