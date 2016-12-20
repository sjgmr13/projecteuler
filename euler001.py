# EP001

def euler001(k):
    a = []
    for i in range(1,k):
        if i%3 == 0 or i%5 == 0:
            a.append(i)
    return sum(j for j in a)
