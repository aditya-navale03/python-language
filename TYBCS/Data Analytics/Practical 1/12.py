n = int(input("Enter a number: "))
rev = int(str(n)[::-1])

if n == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

