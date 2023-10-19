# realiza un algoritmo que le pida al usuario un
# numero y imprima los numeros pares que hay desde cero
# hasta el numero ingresado por el usuairio#

# items 1: pedir una entrad
# item 2: trabajar con un for
# item 3: if


number = int(input("Ingrese un numero: "))

# creo un contador
cont = 0
cont2 = 0

for i in range(1, number):
    if i % 2 == 0:
        print(" ", i)
        cont += i
        cont2 += 1

print("La cantidas de numero pares es: ", cont)
print("La cantidas de numero pares es: ", cont2)
