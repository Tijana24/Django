# ispisivanje trocifrenih brojeva kod kojih je prva cifra jednaka poslednjoj
import math


def prva_jednaka_poslednjoj(broj):
    if broj/10>=10 and broj/10<=100: 
        print("Broj je: ", broj)
        poslednja_cifra=broj%10
        print("Poslednja cifra je: ",poslednja_cifra)
        prva_cifra=broj // 10 ** (int(math.log(broj, 10)) )       
        print("Prva cifra je : ", prva_cifra)
        if prva_cifra==poslednja_cifra:
            print("Ista cifra!")
        else:
            print("Nije ista cifra!")
    else:
        print("Nije trocifren broj!")
    

prva_jednaka_poslednjoj(323)