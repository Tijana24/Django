def prosjecna_temperatura(pon, uto, sri, cet, pet, sub, ned):
    lista=[pon, uto, sri, cet, pet, sub, ned]
    suma=0
    prosjecna=0
    for i in lista:
        suma=suma+i
        
    prosjecna= round((suma/7),2)
    return prosjecna  

x=prosjecna_temperatura(12,15,17,9,8,10,16)
print(x)