# EP010

import math
def euler010(n):
    a = []
    b = 2
    prim = []
    c = 0
    for i in range(2, n):
        a.append(i)
    
    while b<n:
        j = 0
        if len(a) > 0:        
            prim.append(b)
            a.remove(b)
        else:
            pass
        while (b*b+b*j) < n:
            if b*b+b*j in a:
                a.remove(b*b+b*j)
            else:
                pass
            j += 1
        if len(a)>0:        
            b = a[0]
        else:
            break
    
    for prim in prim:
        c += prim
    return(c)
