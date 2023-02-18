import random 

numero=random.randint(1,2)

if numero==1:
   lado="cara"
if numero==2:
   lado="sello"


print("Elige cara o sello")
respuesta=input()


if respuesta==lado:
   print(" ha salido "+lado+", has acertado")

if respuesta !=lado:
   print(" ha salido "+lado+", has perdido")
