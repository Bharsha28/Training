'''ip:
     hello:12345,car:241,at:8899
    op: oax'''
l=list(input().split(","))
l1=[]
for i in range(len(l)):
    l1.append(l[i].split(':'))
print(l1)
res=""
for j in l1:
    for i in range(len(j)):
        ls=len(j[0])
        #print(ls,end=" ")
        s=j[0]
        #print(s,end=" ")
        num=j[1]
        def ele(e,num):
            #print(e)
            if e<0:
                return 0
            if str(e) in num:
                return e
            else:
                return ele(e-1,num)
    t=ele(ls,num)
    #print(type(t),t)
    if t==0:
        res+='x'
    else:
        res+=s[t-1]   
print(res)
    
    