# Python program to find simple interest

def simp(p,t,r):
	SI = (p*t*r) / 100
	return SI

P = int(input("Enter Principal Amount :- "))
T = int(input("Enter Time :- "))
R = int(input("Enter Rate :- "))

print(f"\nSimple Interest for Principal Amount : {P} , Time : {T} and Rate : {R} is {simp(P,T,R)}")
