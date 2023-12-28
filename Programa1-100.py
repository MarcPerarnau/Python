print("*****************************************")
print("*****  Marc Liang Perarnau Olaya    *****")
print("*****************************************")

número = int(input("Escribe un número dentro del rango 1 - 100: "))

if número > 100:
    print(número, "es más grande que 100, no està dentro del rango.")
if número < 1:
    print(número, "es mas pequeño que 1, no està dentro del rango.")
if número >= 1 and número <= 100:
    print(número, "està dentro del rango.")