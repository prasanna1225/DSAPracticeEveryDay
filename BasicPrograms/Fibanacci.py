n=int(input())
a,b,c=0,1,0
print(a, b, end="")
for i in range(1, n):
    c=a+b
    a=b
    b=c
    print(" ", c, end="")