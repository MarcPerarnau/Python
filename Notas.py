print("*****************************************")
print("*****  Marc Liang Perarnau Olaya    *****")
print("*****************************************")

nota = float(input("Introduce la nota del examen [1-10]: "))
if nota < 0 or nota > 10:
    print("Introduce una nota dentro de los parametros")

if nota < 5 and nota > 0:
    print("Suspenso")
    
if nota >= 5 and nota <= 5.99:
    print("Aprobado")
    
if nota >= 6 and nota <= 6.99:
    print("Bien")
    
if nota >= 7 and nota <= 8.99:
    print("Notable")

if nota >= 9 and nota <= 10:
    print("Excelent")