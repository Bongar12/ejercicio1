edad=int(input("Ingrese tu edad en años \n"))
if 0<edad<=4:
    print("El cliente ingresa gratis")

elif 4>edad<18:
    print("El debera pagar 20.000")

elif 18<=edad<=60:        
     print("El debera pagar 15.000")

elif 60>edad:
     print("El debera pagar 3.000")   

else:
     print("Ingrese la edad valida")    
