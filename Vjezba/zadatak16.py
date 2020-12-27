aritmeticka=0
suma=0
suma2=0
brojac=0
brojac2=0
niz=[4,5,6,7,8,7]
for i in niz:
    if i%3!=0:
        suma=suma+i
        brojac=brojac+1
    elif i%3==0:
        break
        suma2=suma2+i
        brojac2=brojac2+1

    aritmeticka=round(((suma+suma2)/(brojac+brojac2)),2)

print("Äritmeticka suma je: ",aritmeticka)        
    

