class Node:
    def __init__(self):
        self.d={}
        self.flag=0
class tries:
    def __init__(self):
        self.root=Node()
    def insert(self,st):
        temp=self.root
        for i in st:
            if i not in temp.d:
                temp.d[i]=Node()
            temp=temp.d[i]
        temp.flag=1
    def search(self,tar):
        temp=self.root
        c=0
        for i in tar:
            if i in temp.d:
                c+=1
                temp=temp.d[i]
            else:
                print("False")
                break
        if c==len(tar):
            print("True")
    def prefix(self,pre):
        temp=self.root
        c=0
        for i in pre:
            if i in temp.d:
                c+=1
                temp=temp.d[i]
        if c==len(pre):
            print("True")
        else:
            print("False")
    def prefix_word(self,pre):
        temp=self.root
        res=""
        for i in pre:
            if i in temp.d:
                res+=i
                temp=temp.d[i]
        if len(res)!=0:
            def helper(temp,l,res):
                if temp.flag==1:
                    l.append(res)
                for i in temp.d:
                    res+=i
                    #print(res)
                    helper(temp.d[i],l,res)
                    #res=res[:-1]
                return l
            t=helper(temp,[],res)
            print(t)
        else:
            print("False")
    def longest_prefix(self,l,max1,res):
        temp=self.root
        c=0
        for i in l:
            s=""
            for j in i:
                if j in temp.d:
                    c+=1
                    s+=j
                    temp=temp.d[j]
            if c>max1:
                max1=c
                res=s
        print(res,c)
        
obj=tries()
print("Enter no.of strings to insert")
n=int(input())
for i in range(n):
    s=input()
    obj.insert(s)
'''print("Enter string to search")
tar=input()
obj.search(tar)'''
print("enter prefix string to search")
pre=input()
obj.prefix(pre)
obj.prefix_word(pre)
l=['b','ba','wo','ap']
obj.longest_prefix(l,0,"")
'''4
word
words
world
wood'''
    