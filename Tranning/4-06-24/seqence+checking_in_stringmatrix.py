#seqence of a string in a matrix row wiseSS
n=int(input())
l=[]
for i in range(n) :
        k=input()
        l.append(list(k))
print(l)
word=input()
c=0
l1=[]
for i in range(n):
    if (word[i] in l[i%n]):
        l[i].remove(word[i])
        continue
    else:
            print("No")
            c=1
            break
if c==0:
    print("yes")

        