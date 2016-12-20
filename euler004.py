# EP004

def euler004(k,l):
    pal_list = []
    prod_a = []
    prod_b = []
    for a in range(k,l+1):
        for b in range(k,l+1):
            n = a*b
            lista = []
            while (n>0):
                lista.append(n%10)
                n=n//10
            
            for i in range (0,len(lista)):
                if lista[i] == lista[len(lista)-i-1]:
                    pal = True
                else:
                    pal = False
                    break
                    
            if pal:
                pal_list.append(a*b)
                prod_a.append(a)
                prod_b.append(b)
    return max(pal_list), prod_a[pal_list.index(max(pal_list))], prod_b[pal_list.index(max(pal_list))]
                
