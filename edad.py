import time
print("*****************************************")
print("*****  Marc Liang Perarnau Olaya    *****")
print("*****************************************")
current_time = time.localtime()
current_year = current_time.tm_year
print("Como quieres que hagamos el calculo.")
print("1. - Adivinemos los años con tu fecha de nacimiento")
print("2. - Adivinemos el año de nacimiento con tu edad.")
como = int(input("[1-2]: "))
if como == 1:
    año = int(input("Introduce solo tu año de nacimiento: "))
    edad = current_year - año
    print("Tienes" ,edad, "años.")
if como == 2:
    edad = int(input("Introduce tu edad: "))
    año = current_year - edad
    print("Si tienes", edad, "naciste el año", año)