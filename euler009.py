# EP009

def euler009(n):
    a = [1, 1, 1]
    b = []
    c = []
    for i in range(n):
        for j in range(n):
            a = [1+i, 1+j, n-(2+i+j)]
            if a[0]<a[1]<a[2] and a[0]*a[0] + a[1]*a[1] == a[2]*a[2]:
                    b.append(a)
                    c.append(a[0]*a[1]*a[2])
            else:
                pass
    return print(b,c)
