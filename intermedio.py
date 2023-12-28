print("*****************************************")
print("*****  Marc Liang Perarnau Olaya    *****")
print("*****************************************")

numero_inicial = int(input("Introduce el número inicial: "))
numero_final = int(input("Introduce el número final: "))
if numero_inicial > numero_final:
    print("El número inicial no puede ser mayor que el número final.")
else:
    numero = numero_inicial
    while numero <= numero_final:
        print(numero)
        numero += 1