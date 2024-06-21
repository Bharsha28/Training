n=int(input())
l=[]
for i in range(n):
    q=int(input())
    s=input()
    l.append((q,s))
l2=[]
for i in range(len(l)):
    if l[i][0]==1:
        if l[i][0] not in l2:
            l2.append(l[i][1])
    if l[i][0]==2:
        if l[i][1] in l2:
            print("True")
        else:
            print("False")
    if l[i][0]==3:
        le=len(l[i][1])
        c=0
        for j in l2:
            s=j
            if l[i][1]==s[:le]:
                c+=1
        if c==0:
            print("False")
        else:
             print(c)
    if l[i][0]==4:
        if l[i][1] in l2:
            l2.remove(l[i][1])
