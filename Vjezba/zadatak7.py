#rastavljanje prirodnog broja na proste

import math

def get_proste_cinioce(broj):
    prosti_cinioci = [1]

    while broj % 2 == 0:
        prosti_cinioci.append(2)
        broj = broj / 2
    
    for i in range(3, int(math.sqrt(broj)) + 1, 2):
        while broj % i == 0:
            prosti_cinioci.append(int(i))
            broj = broj / i
    
    if broj > 2:
        prosti_cinioci.append(int(broj))

    return prosti_cinioci

x=int(input("Unesite prirodan broj: "))
print(get_proste_cinioce(x))
