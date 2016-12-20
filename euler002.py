# EP002

def fib_first_n_list(n):
    fib_seq = []
    if n == 0:
        fib_seq
    elif n == 1:
        fib_seq = [1]
    elif n == 2:
        fib_seq = [1,2]
    elif n > 2:
        fib_seq = [1,2]
        for i in range(2,n):
            fib_seq.append(fib_seq[i-2] + fib_seq[i-1])    
    return fib_seq

def euler002(k):
    i = 3
    while (fib_first_n_list(i)[-1]<k):
        fib_first_n_list(i)
        i += 1
    return sum(a for a in fib_first_n_list(i-1) if a%2 == 0)
