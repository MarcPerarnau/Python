print("*****************************************")
print("*****  Marc Liang Perarnau Olaya    *****")
print("*****************************************")

num_incial = 1
numero = int(input("Introduce un número mayor que 1: "))
if numero < 1:
    print("El número introducido no entra dentro de los parametros.")
else:
    while num_incial <= numero:
        print(num_incial)
        num_incial += 1