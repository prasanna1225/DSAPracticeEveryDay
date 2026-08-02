n=int(input())
temp=n
sum=0
while n>0:
    r=n%10
    sum=sum*10+r
    n//=10
if temp==sum:
    print("palindrom")
else:
    print("not palindrom")

