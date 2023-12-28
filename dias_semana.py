print("*****************************************")
print("*****  Marc Liang Perarnau Olaya    *****")
print("*****************************************")

numero = int(input("Escribe un número del 1 - 7: "))
if numero == 1:
    print("Lunes")
if numero == 2:
    print("Martes")
if numero == 3:
    print("Miercoles")
if numero == 4:
    print("Jueves")
if numero == 5:
    print("Viernes")
if numero == 6:
    print("Sabado")
if numero == 7:
    print("Domingo")
if numero < 1 or numero > 7:
    print("El número es invalido")