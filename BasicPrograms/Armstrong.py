def is_armstrong(n):
    temp = n
    digits = 0
    total = 0

    while temp > 0:
        temp //= 10
        digits += 1

    if n == 0:
        digits = 1

    temp = n


    while temp > 0:
        last = temp % 10
        total += last ** digits
        temp //= 10

    return total == n


num = int(input("Enter the number: "))

if is_armstrong(num):
    print("Armstrong")
else:
    print("Not Armstrong")