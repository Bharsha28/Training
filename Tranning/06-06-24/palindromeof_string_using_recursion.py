def word(s,i,j):
     if i>=j:
        return 1
     elif s[i]==s[j-1]:
         i+=1
         j-=1
     else:
        return 0
     return word(s[i:j+1],i,j)
s="amanaplanacanalpanama"
print(word(s,0,len(s)-1))
def isPalindrome(s):
        t=""
        for i in s:
            if i.isalnum():
                t+=i
        if len(t)<=1:
            return 1
        else:
            def help1(t,i,j):
                if i>=j:
                    return 1
                elif t[i]==t[j]:
                    i+=1
                    j-=1
                    t=t[i:j+1]
                else:
                    return 0
                return help1(t,i,j)
            k=help1(t,0,len(t)-1)
        return k
s="A man, a plan, a canal: Panama"
print(isPalindrome(s))