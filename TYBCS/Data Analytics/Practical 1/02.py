# Python program to find maximum of two numbers 

def max(x,y):
    if(x>y):
        return x
    else:
        return y

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print(f"Maximum number between {a} and {b} is :- {max(a,b)}")
