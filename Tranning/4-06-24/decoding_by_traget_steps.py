n=input()
key=int(input())
s=""
#key=key%26
for i in range(len(n)):
    p=ord(n[i])
    if (p-key)<ord('a'):
        p=(p+26)-key
        s+=chr(p)
    elif (p-key)>ord('z'):
        p=(p-26)-key
        s+=chr(p)
    else:
        p=p-key
        s+=chr(p)
print(s)

