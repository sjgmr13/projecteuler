# EP003

import math

def euler003(n):
    number = n
    fact = []
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        while (number % i == 0 ):
            number=number//i
            fact.append(i)   
    if number != 1:
        fact.append(number)
    return fact[-1]
