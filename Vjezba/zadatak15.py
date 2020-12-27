
import math
def stepenovanje(a,b):
    aa=a+a
    abba=a+b+b+a
    if math.pow(aa,b)==abba:
        return "Yes!"
    else:
        return "NO!"


print(stepenovanje(1,2))
