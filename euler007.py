# EP007

import math

def euler007(k):
    prim_lista = []
    i = 2
    while (len(prim_lista)<k):
        if isprime(i):
            prim_lista.append(i)
            i += 1
        else:
            i += 1
    return prim_lista[-1]
        


def isprime(k):
    prime_fact = []
    for i in range(2,math.ceil(math.sqrt(k))+1):
        while(k%i == 0):
            k = k//i
            prime_fact.append(i)
    if k>1:
        prime_fact.append(k)
    prim_osztok = list(set(prime_fact))
    prim_osztok_multiplicitasa = []
    for i in prim_osztok:
        prim_osztok_multiplicitasa.append(prime_fact.count(i))
    prim = dict(zip(prim_osztok, prim_osztok_multiplicitasa))
    if len(prim.keys()) == 1 and list(prim.values()) == [1]:
        return True
    else:
        return False
