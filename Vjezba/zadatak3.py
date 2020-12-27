def pronadji_maksimum(broj):
    racunaj=[0 for x in range(10)]
    string=str(broj)
    for i in range(len(string)):
        racunaj[int(string[i])]=racunaj[int(string[i])]+1

    rezultat=0
    multiplier=1

    for i in range(10):
        while racunaj[i]>0:
            rezultat=rezultat+(i*multiplier)
            racunaj[i]=racunaj[i]-1
            multiplier=multiplier*10
    return rezultat


x=int(input("Unesite broj: "))
print(pronadji_maksimum(x))