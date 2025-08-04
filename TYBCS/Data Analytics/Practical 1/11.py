def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

n = int(input("Enter a number: "))

if is_perfect(n):
    print("Perfect Number")
else:
    print("Not a Perfect Number")

