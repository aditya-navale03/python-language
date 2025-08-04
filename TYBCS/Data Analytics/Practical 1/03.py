# Python program to find factorial of a number

def fact(n):
    if(n==1):
        return 1
    return n * fact(n-1)

a = int(input("Enter any number to get it's factorial :- "))
print(f"\nFactorial of {a} is {fact(a)}")
