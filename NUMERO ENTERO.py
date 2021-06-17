X=int(input("Ingresa un numero entero: "))
if X < 0:
    X = 0
    print('Negativo cambiado a cero')
elif X == 0:
    print('Cero')
elif X == 1:
     print("Uno")
else:
     print("Ninguna opcion")
print("Ok") if type(X) == int else print("-")