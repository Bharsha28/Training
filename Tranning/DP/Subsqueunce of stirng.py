"""
ip:-
    given 2 strings
    abcd
    axbdc
op:-
    print all the sub sequence
    abcd-a,ab,ac,ad,abc,abd,abcd,b,bc,bd,bcd,c,cd,d
"""
res=[]
def all_sub_sequence(s,res_s):
    if res_s not in res:
        res.append(res_s)
    if not s:
        return
    all_sub_sequence(s[1:],res_s+s[0])
    all_sub_sequence(s[1:],res_s)
def sub_sequence(s):
    for i in range(len(s)):
        all_sub_sequence(s[i+1:],s[i])

s="abcdx"
sub_sequence(s)
print(res)
from itertools import permutations
a="abcd"
s=[]
for i in range(1,len(a)):
    per=permutations("abcd",i)
    s.append(list(per))
print(s)





