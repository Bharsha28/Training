'''Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21'''
n=int(input())
m=n
l=str(n)
def reverse(s,n,m):
    if n==0:
        if m>0:
            return s+l[0]
        elif m<0:
            return l[0]+s
    if m%10==0:
        m=m//10
        return reverse(s,n-1,m)
    else:
        s+=l[n]
        return reverse(s,n-1,m)
print(reverse("",len(l)-1,m))
def reverse(n):
    s=str(n)
    if n%10==0:
        m=s[::-1]
        return m[1:]
    elif n>0:
        return s[::-1]
    elif n<0:
        m=s[1:]
        return s[0]+m[::-1]
print(reverse(n))

