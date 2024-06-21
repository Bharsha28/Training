"""abfgresagtyuiofde"""
s=input()
max1=0
'''for i in range(len(s)):
    s1=""
    for j in range(i,len(s)):
        if s[j] not in s1:
            s1+=s[j]
        else:
            max1=max(max1,len(s1))
            break
print(max1)'''
i=0
j=0
s1=""
while(i<=len(s)-1):
    if  j>len(s)-1:
        j=i
    if s[j] not in s1:
        s1+=s[j]
    else:
        s1=""
        i+=1
        j=i-1
    j+=1
    max1=max(max1,len(s1))
print(max1)
"""
ip:-
    take input of the string
    abfgresagtyuiofde
op:-
    print longest sub string without repeating character
    12 resagtyuiofd
"""
s=input()
d=dict()
d[s[0]]=0
mx=-1
j=0
n=len(s)
i=1
while i<n:
    if s[i] not in d:
        d[s[i]]=i
    else:
        if mx<i-j:
            mx=i-j
        if d[s[i]]>j:
            j=d[s[i]]+1
        d[s[i]]=i
    i+=1
if mx<(i-j):
    mx=i-j
print(mx)
