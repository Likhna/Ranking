from math import sqrt

def _confidence(plus, minus):
    n = plus + minus

    if n == 0:
        return
z=3;
    phat = float(plus) / n
    return sqrt(phat+z*z/(2*n)-z*((phat*(1-phat)+z*z/(4*n))/n))/(1+z*z/n)

def confidence(plus, minus):
    if plus + minus == 0:
        return 0
    else:
        return _confidence(plus, minus)
