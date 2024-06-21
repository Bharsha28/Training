
n=int(input())
'''ip:122
  op:131'''
s=str(n)
if s==s[::-1]:
    print("yes")
else:
    res=""
    if len(s)%2==0:
        s1=s[:len(s)//2]
        s2=s[len(s)//2:]
        if int(s1)>=int(s2):
            res+=s1+s1[::-1]
            print(res)
        else:
            r=int(s1[-1])+1
            s3=s1[:-1]+str(r)
            print(s3+s3[::-1])
    else:
        s1=s[:len(s)//2]
        mid=s[len(s)//2]
        s2=s[len(s)//2+1:]
        #print(s1,s2,mid)
        if int(s1)>=int(s2):
            s3=s1+mid+s1[::-1]
            print(s3)
        else:
            s1=s[:len(s)//2+1]
            rev=s1[:len(s)//2]
            r=int(s1[-1])+1
            s3=rev+str(r)+rev[::-1]
            print(s3)
        
