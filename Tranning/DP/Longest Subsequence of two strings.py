'''ip:-
    given 2 strings
    abcd
    axbdc
    op:
    3,abd'''

s1="abcd"
s2="axd"
#l=[[0 for i in range(len(s)+1)] 0 for j in range(len(s1)+1)]
sub=[]
m=len(s2)+1
for i in range(len(s1)+1):
    l=[0]*m
    sub.append(l)
for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            sub[i][j]=sub[i-1][j-1]+1
        else:
            sub[i][j]=max(sub[i][j-1],sub[i-1][j])
print(sub[len(s1)][len(s2)])
s=""
u=len(s1)
v=len(s2)
while(u!=0 and v!=0):
   if s1[u-1]==s2[v-1]:
       s+=s1[u-1]
       u=u-1
       v=v-1
   else:
        if sub[u][v]==sub[u-1][v]:
            u=u-1
        else:
            v=v-1
print(s[::-1])

            