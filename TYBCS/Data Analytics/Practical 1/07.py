# Python program to find area of circle
import math

def area(r):
	return math.pi * (r**2)

r = float(input("Enter value of radius to find it's area of circle :- "))
print(f"Area of circle for radius : {r} is {area(r)}")
