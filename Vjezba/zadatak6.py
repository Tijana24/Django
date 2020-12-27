#Provjera da li je broj prost ili nije

x=int(input("Unesite broj: "))

if x > 1:
   for i in range(2,x):
        if (x % i) == 0:
           print(x,"Nije prost broj!")
           break
        else:
            print(x,"Prost je broj!")
            break
else:
   print(x,"Nije prost broj!")

