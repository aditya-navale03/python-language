# Python program to check whether a number is armstrong number 

def checkarm(n):
	a = str(n)
	l = len(a)
	x = 0
	for i in a:
		x = x + (int(i)**l)
	if(x==n):
		return True

n = int(input("Enter a number to check if it's armstrong or not :- "))
if(checkarm(n)):
	print("Given number is an armstrong.")
else:
	print("Given number is not an armstrong.")
