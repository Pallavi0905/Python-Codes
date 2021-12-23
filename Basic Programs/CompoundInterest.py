# A = P(1 + R/100) t 
# Compound Interest = A – P 
# Where, 
# A is amount 
# P is principle amount 
# R is the rate and 
# T is the time span
def compound_interest(p,r,t):
    print('Enter the Principal Amount: ',p)
    print('Enter the rate of interest: ',r)
    print('Enter the time(in years): ',t)

    Amount = p * (pow((1+r/100), t))
    CI = Amount - p
    print(f"Compound Interest is {CI}")

compound_interest(10000,10.25,5)
