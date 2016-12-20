# EP005

import math

def prime_fact(k):
    prime_fact = []
    for i in range(2, math.ceil(math.sqrt(k)) + 1):
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
    return prim

def euler005(n):
    prim_osztok_max_multiplicitas = {}
    for i in range(2, n+1):
        for j in prime_fact(i).keys():
            if j not in prim_osztok_max_multiplicitas.keys():
                prim_osztok_max_multiplicitas[j] = prime_fact(i)[j]
            elif j in prim_osztok_max_multiplicitas.keys():
                if prim_osztok_max_multiplicitas[j] < prime_fact(i)[j]:
                    prim_osztok_max_multiplicitas[j] = prime_fact(i)[j]
                else:
                    prim_osztok_max_multiplicitas[j]
    
    lkkt = 1
    for l in prim_osztok_max_multiplicitas.keys():
        a = prim_osztok_max_multiplicitas[l]
        while a>0:
            lkkt *= l
            a -= 1
        
    return lkkt
