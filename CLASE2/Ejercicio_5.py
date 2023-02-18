Leche=input("¿Trajo la leche? \n Digite s o n \n")
pan=input("¿Trajo el pan?\n Digite s o no \n")
huevos=input("¿Trajo los huevos? \n Digite s o n \n")

#mama estricta
if Leche=="S" and pan=="s" and huevos=="s":
    print("Era lo minimo venga y desayuna")

else:
     print("chanclazo")

#mama comprensiva
if Leche=="s" or pan=="s"  or huevos=="s":
    print("Bueno mi amor")

else:
    print("ay me va a tocar ir a mi")
