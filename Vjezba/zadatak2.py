# racunanje korijena najvece cifre unijetog trocifrenog broja
import math

x= int(input("Unesite trocifren broj:  "))
 
jedinica=x%10
y=x//10
desetica=y%10
stotina=y//10

maksimum=0
skup=[jedinica,desetica,stotina]

for element in skup:
    if element>maksimum:
        maksimum=element
print("Korijen maksimalnog broja je :")
print(math.sqrt(maksimum))


