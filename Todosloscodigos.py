import math
import os
import time
print("*****************************************")
print("*****  Marc Liang Perarnau Olaya    *****")
print("*****************************************")

#Funcion para limpiar la pantalla
def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')
#Funciones del programa Operaciones matematicas
def operaciones():
    print("Que operacion matematica quieres hacer?")
    print("1. - Sumar")
    print("2. - Restar")
    print("3. - Multiplicar")
    print("4. - Dividir")
    print("5. - Raiz Cuadrada")
    Pregunta_usuari = int(input("[1-5]: "))

    if Pregunta_usuari == 1:
        Numero1 = int(input("Introduce el primer número para sumar: "))
        Numero2 = int(input("Introduce el segundo número para sumar: "))
        suma = Numero1 + Numero2
        print("*****************************************")
        print("La suma de", Numero1, "+", Numero2, "es:", suma)

    if Pregunta_usuari == 2:
        Numero1 = int(input("Introduce el primer número para restar: "))
        Numero2 = int(input("Introduce el segundo número para restar: "))
        resta = Numero1 - Numero2
        print("*****************************************")
        print("La resta de", Numero1, "-", Numero2, "es:", resta)

    if Pregunta_usuari == 3:
        Numero1 = int(input("Introduce el primer número para multiplicar: "))
        Numero2 = int(input("Introduce el segundo número para multiplicar: "))
        multi = Numero1 * Numero2
        print("*****************************************")
        print("La multiplicacion de", Numero1, "x", Numero2, "es:", multi)

    if Pregunta_usuari == 4:
        Numero1 = int(input("Introduce el primer número para dividir: "))
        Numero2 = int(input("Introduce el segundo número para dividir: "))
        divi = Numero1 / Numero2
        print("*****************************************")
        print("La division de", Numero1, "/", Numero2, "es:", divi)

    if Pregunta_usuari == 5:
        Numero1 = int(input("De que número quieres saber la raiz cuadrada: "))
        cua = math.sqrt(Numero1)
        print("*****************************************")
        print("La raiz cuadrada de", Numero1, "es:", cua)
#Funciones del programa Notas
def notas():
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
#Funciones del programa area del triangulo
def area():
    base = float(input("Introduce la base del triangulo: "))
    altura = float(input("Introduce la altura del triangulo: "))
    multi = base * altura
    divi = multi / 2
    print("La area del triangulo es:", divi)
#Funciones del programa comparar números
def comparar():
    Número1 = float(input("Introduce el primer número para comparar: "))
    Número2 = float(input("Introduce el segundo número para comparar: "))
    if Número1 < Número2:
        print(Número2, "es mayor que", Número1)
    if Número1 > Número2:
        print(Número1, "es mayor que", Número2)
    else:
        print("Los números son iguales")
#Funciones del programa par e impar
def pareimpar():
    Número = int(input("Introduce un número y te dire si es par o impar: "))
    if Número % 2 == 0:
        print("El número", Número, "es par.")
    else:
        print("El número", Número, "es impar.")
#Funciones del programa positivo negativo
def positivo_negativo():
    Numero = float(input("Escribe un numero y te dire si es positivo o negativo: "))
    if Numero < 0:
        print("El número", Numero, "es negativo.")
    if Numero >= 0:
        print("El número", Numero, "es positivo.")
#Funciones del programa rango
def rango():
    número = int(input("Escribe un número dentro del rango 1 - 100: "))
    if número > 100:
        print(número, "es más grande que 100, no està dentro del rango.")
    if número < 1:
        print(número, "es mas pequeño que 1, no està dentro del rango.")
    if número >= 1 and número <= 100:
        print(número, "està dentro del rango.")
#Funciones del programa año bisiesto
def año():
    año = int(input("Escribe el año para saber si es bisiesto: "))
    if año % 4 == 0:
        print("El", año, "es bisiesto.")
    else:
        print("El", año, "no es bisiesto.")
#Funciones del programa números en bucle
def bucle():
    ar = [] # Definir ar como lista vacía
    for i in range(5):
        print("Introduce números:")
    ar.append(input()) # Leer y agregar el número ingresado a la lista ar
    print("***************************************")
    for i in range(5):
        print(ar[i]) # Mostrar el elemento i de la lista ar
#Funciones del programa caracter unico
def caracter():
    caracter = input("Introduce un caracter: ")
    longitud = len(caracter)
    if longitud == 1:
        print("Cumples los requisitos.")
    else:
        print("El valor introducido no cumple los requisitos indicados.")
#Funciones del programa dias de la semana
def dias_semana():
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
#Funciones del programa números intermedios
def intermedio():
    numero_inicial = int(input("Introduce el número inicial: "))
    numero_final = int(input("Introduce el número final: "))
    if numero_inicial > numero_final:
        print("El número inicial no puede ser mayor que el número final.")
    else:
        numero = numero_inicial
        while numero <= numero_final:
            print(numero)
            numero += 1
#Funciones del programa calculadora edad
def edad():
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
#Funciones del programa números procesedores
def numerosantes():
    num_incial = 1
    numero = int(input("Introduce un número mayor que 1: "))
    if numero < 1:
        print("El número introducido no entra dentro de los parametros.")
    else:
        while num_incial <= numero:
            print(num_incial)
            num_incial += 1
#Funciones del programa partido de padel


P = "si"
while P == "si":
    print("Que programa quieres ejecutar?")
    print("01. - Operaciones matemáticas")
    print("02. - Notas")
    print("03. - Calcular area del triangulo")
    print("04. - Comparar números")
    print("05. - Par e impar")
    print("06. - Números positivos o negativos")
    print("07. - Números dentro del rango.")
    print("08. - Año bisiesto.")
    print("09. - Números en bucle")
    print("10. - Dias de la semana")
    print("11. - Números intermedios")
    print("12. - Calculadora de edad")
    print("13. - Números presecedores")
    print("14. - Partido de padel")
    Pregunta = int(input("[1- 14]:"))
    
    if Pregunta == 1:
        operaciones()
    if Pregunta == 2:
        notas()
    if Pregunta == 3:
        area()
    if Pregunta == 4:
        comparar()
    if Pregunta == 5:
        pareimpar()
    if Pregunta == 6:
        positivo_negativo()
    if Pregunta == 7:
        rango()
    if Pregunta == 8:
        año()
    if Pregunta == 9:
        bucle()
    if Pregunta == 10:
        dias_semana()
    if Pregunta == 11:
        intermedio()
    if Pregunta == 12:
        edad()
    if Pregunta == 13:
        numerosantes()
    if Pregunta == 14:
        ()
    
    P = input("Quieres volver al menu?[si/no]:")
    if P == "si":
        limpiar()
    if P == "no":
        print("Chao, chao, ha sido un placer. :)")
