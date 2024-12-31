import math
def bongden(m,n,d):
    if m>n or d>n:
        return 'Invalid'
    else:
        P=(math.comb(d,1)*math.comb(n-d,m-1)/math.comb(n,m))
        return P
n=int(input('Enter number of light bulbs:'))
m=int(input('Enter number of picked light bulbs:'))
d=int(input('Enter number of damaged light bulbs:'))
print(bongden(m,n,d))