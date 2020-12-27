# dvocifreni parni brojevi

def izvuci_dvocifrene_parne_brojeve(lista):
    nova_lista=[]
    for broj in lista:
        if broj/10<10 and broj/10>1 and broj%2==0:
            nova_lista.append(broj)
    print("Dvocifreni parni brojevi su : ",nova_lista)

x=[24,456,789,1,11,478,520, 12, 56, 13, 123, 24]
izvuci_dvocifrene_parne_brojeve(x)
