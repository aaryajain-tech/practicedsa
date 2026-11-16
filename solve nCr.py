def fact(num):
    f=1
    if num==0:
        return 1
    else:
        for i in range(1,num+1):
            f=f*i
        return f
n=int(input("Enter a value for n:"))
r=int(input("Enter a value for r:"))
# nCr=fact(n)/(fact(r)*fact(n-r))
factn=fact(n)
factr=fact(r)
factnr=fact(n-r)
nCr=factn/(factr*factnr)
print("The value of nCr is:",int(nCr))