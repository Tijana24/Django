#Provjera da li je druga cifra trocifrenog broja parna ili neparna

x= int(input("Unesite trocifren broj:  "))
x=x//10
y=x%10

if y%2!=0 :
    print("Neparan")

elif y==0:
    print("Naisli smo na nulu.")    

else: 
    print("Paran")


    