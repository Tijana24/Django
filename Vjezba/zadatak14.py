# 0 prekida unos brojeva, vraca broj poyitivnih i negativnih brojeva

pozitivni=[]
neg=0
negativni=[]
poz=0
x=[1,2,3,4,0]
for i in x:
    if i>0:
        pozitivni.append(i)
        poz=poz+1
    elif i<0:
        negativni.append(i)
        neg=neg+1
    else:
        break
    
            

print("Pozitivni brojevi su: ", pozitivni, "i ima ih:", poz)
print("Negativni brojevi su: ", negativni, "i ima ih:", neg)          
print("Naisli smo na nulu, dalje se prekida!")