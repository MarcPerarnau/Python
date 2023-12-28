print("*****************************************")
print("*****  Marc Liang Perarnau Olaya    *****")
print("*****************************************")

año = int(input("Escribe el año para saber si es bisiesto: "))

if año % 4 == 0:
    print("El", año, "es bisiesto.")
else:
    print("El", año, "no es bisiesto.")