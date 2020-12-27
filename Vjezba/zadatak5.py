def operacija(clan1, clan2, op):
    if op==1:
        return clan1+clan2
    elif op==2:
        return clan1-clan2
    elif op==3:
        return clan1*clan2
    elif op==4:
        return clan1/clan2
    else:
        return "Kriva operacija!"

x=operacija(2,7,5)
print("Rezultat operacije je: ", x)    