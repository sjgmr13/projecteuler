# EP008

import numpy as np
def euler008(n,k):
    n_list = []
    while (n>0):
        n_list.append(n%10)
        n = n//10
    n_list.reverse()
    max_hely = list(range(k))
    max_hely_list = [n_list[i] for i in max_hely]
    max_ertek = np.product([float(x) for x in max_hely_list])
    for j in range(1, len(n_list) - (k+1)):
        max_hely_leh = list(range(j, j+k))
        max_hely_leh_list = [n_list[i] for i in max_hely_leh]
        max_leh_ertek = np.product([float(x) for x in max_hely_leh_list])
        print(max_leh_ertek)
        if max_leh_ertek > max_ertek:
            max_hely = max_hely_leh
            max_hely_list = max_hely_leh_list
            max_ertek = max_leh_ertek
        else:
            pass
    return int(max_ertek), max_hely, max_hely_list
