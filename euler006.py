# EP006

def sumsq_nat(n):
    a = 0
    for i in range(1, n+1):
        a += i*i
    return a

def sum_sq_nat(k):
    a = 0
    for i in range(1, k+1):
        a += i
    return a*a

def euler006(l):
    return sum_sq_nat(l) - sumsq_nat(l)
