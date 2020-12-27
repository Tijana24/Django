#selekcija dvocifrenuh brojeva

def izvuci_dvocifrene_brojeve(lista):
    nova_lista=[]
    for broj in lista:
        if broj/10<10 and broj/10>1:
            nova_lista.append(broj)
    print(nova_lista)

x=[24,456,789,1,11,478,520]
izvuci_dvocifrene_brojeve(x)
