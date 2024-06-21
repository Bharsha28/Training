''' ip=10
    op=3 7
     we have to print the sum if prime numbers which will be equal to n'''
n=int(input("Enter number"))
def valid(n,i,j):
    if i>j:
        return 
    else:
        def prime(i,j):
            c=0
            for k in range(2,(i//2)+1):
                if i%k==0:
                        c+=1
            if c!=0:
                return 0
            else:
                for k in range(2,(j//2)+1):
                    if j%k==0:
                        c+=1
            if c==0:
                return 1
            else:
                return 0
        if prime(i,j) and n==(i+j):
               return (i,j)
        else:
              return valid(n,i+1,j-1)
print(valid(n,2,n-2)) 