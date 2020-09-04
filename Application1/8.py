import math as m

x=1.2
k=1
N=25
s=x
sign=1.0

while k<N:
    sign=-sign
    k=k+2
    term=sign*x**k/m.factorial(k)
    s=s+term

print('sin(%g) = %g (approximation with %d terms)' % (x,s,N))