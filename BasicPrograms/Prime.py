n=int(input())
flag=0
m=n//2
if n<=1:
    print("Not prime")
else:
    for i in range(2, m):
        if n%i==0:
            print("not prime")
            flag=1
            break

if flag==0:
    print("prime number")

