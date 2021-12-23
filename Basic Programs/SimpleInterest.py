# simple interest = (P x R x T)/100
def simple_interest(p,r,t):
    print('Enter the Principal Amount: ',p)
    print('Enter the rate of interest: ',r)
    print('Enter the time(in years): ',t)
    si = (p * r * t)/100
    print(si)


simple_interest(21000,2,2)