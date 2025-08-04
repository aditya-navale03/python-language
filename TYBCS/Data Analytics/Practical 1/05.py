# Python program to find compund interest

def comp(principal, annual_rate, years, compounding_frequency):
    
    future_value = principal * (pow((1 + annual_rate / compounding_frequency), (compounding_frequency * years)))

    compound_interest = future_value - principal

    return compound_interest

principal_amount = int(input("Enter principal amount :- "))  # Initial investment
interest_rate = float(input("Enter interest rate :- "))      # 5% annual interest rate
time_in_years = int(input("Enter time(in years) :- "))          # Investment period of 3 years
compounding_per_year = int(input("Enter compounding(per year) :- "))  # Compounded monthly

ci = comp(principal_amount, interest_rate, time_in_years, compounding_per_year)

print(f"Compound Interest Earned: ${ci:.2f}")
