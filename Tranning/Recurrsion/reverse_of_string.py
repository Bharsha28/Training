"reverse of string using recurssion "
s=input()
def reverse(string,n):
    if n==-1:
        return string
    string+=s[n]
    return reverse(string,n-1)
print(reverse("",len(s)-1))
