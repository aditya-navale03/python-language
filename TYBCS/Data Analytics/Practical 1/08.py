def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def print_primes_in_interval(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for number in range(start, end + 1):
        if is_prime(number):
            print(number, end=' ')
    print()  # For newline after printing all primes

# Example usage:
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))
print_primes_in_interval(start, end)

