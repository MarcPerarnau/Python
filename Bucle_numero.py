print("*****************************************")
print("*****  Marc Liang Perarnau Olaya    *****")
print("*****************************************")

ar = [] # Definir ar como lista vacía

for i in range(5):
    print("Introduce números:")
    
    ar.append(input()) # Leer y agregar el número ingresado a la lista ar
    print("***************************************")

for i in range(5):
    print(ar[i]) # Mostrar el elemento i de la lista ar