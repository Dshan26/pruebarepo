numbers = int(input("Ingrese un numero de 3 cifras: "))  # entrada: 345     salidas:543

numero1 = numbers // 100  # 3
print("Primer numero ", numero1)
numero2 = (numbers % 100) // 10  # 4
print("segundu numero ", numero2)
numero3 = numbers % 10  # 5
print("tercer numero ", numero3)

numero_invertido = numero3 * 100 + numero2 * 10 + numero1
print("EL numero invertido es: ", numero_invertido)
