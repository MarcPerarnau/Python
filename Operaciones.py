import math
print("*****************************************")
print("*****  Marc Liang Perarnau Olaya    *****")
print("*****************************************")

def sumar():
    Numero1 = int(input("Introduce el primer número para sumar: "))
    Numero2 = int(input("Introduce el segundo número para sumar: "))
    suma = Numero1 + Numero2
    print("*****************************************")
    print("La suma de", Numero1, "+", Numero2, "es:", suma)

def restar():
    Numero1 = int(input("Introduce el primer número para restar: "))
    Numero2 = int(input("Introduce el segundo número para restar: "))
    resta = Numero1 - Numero2
    print("*****************************************")
    print("La resta de", Numero1, "-", Numero2, "es:", resta)

def multiplicar():
    Numero1 = int(input("Introduce el primer número para multiplicar: "))
    Numero2 = int(input("Introduce el segundo número para multiplicar: "))
    multi = Numero1 * Numero2
    print("*****************************************")
    print("La multiplicacion de", Numero1, "x", Numero2, "es:", multi)

def dividir():
    Numero1 = int(input("Introduce el primer número para dividir: "))
    Numero2 = int(input("Introduce el segundo número para dividir: "))
    divi = Numero1 / Numero2
    print("*****************************************")
    print("La division de", Numero1, "/", Numero2, "es:", divi)

def raiz():
    Numero1 = int(input("De que número quieres saber la raiz cuadrada: "))
    cua = math.sqrt(Numero1)
    print("*****************************************")
    print("La raiz cuadrada de", Numero1, "es:", cua)


print("Que operacion matematica quieres hacer?")
print("1. - Sumar")
print("2. - Restar")
print("3. - Multiplicar")
print("4. - Dividir")
print("5. - Raiz Cuadrada")
Pregunta_usuari = int(input("[1-5]: "))

if Pregunta_usuari == 1:
    sumar()

if Pregunta_usuari == 2:
    restar()

if Pregunta_usuari == 3:
    multiplicar()

if Pregunta_usuari == 4:
    dividir()

if Pregunta_usuari == 5:
    raiz()