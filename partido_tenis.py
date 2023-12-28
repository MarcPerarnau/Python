print("*****************************************")
print("*****  Marc Liang Perarnau Olaya    *****")
print("*****************************************")

jugador1 = input("Ingrese el nombre del primer jugador: ")
jugador2 = input("Ingrese el nombre del segundo jugador: ")

puntos_jugador1 = 0
puntos_jugador2 = 0

while True:
    print(f"Puntuación actual: {jugador1}: {puntos_jugador1} - {jugador2}: {puntos_jugador2}")

    ganador_punto = input("Ingrese el número del jugador que ganó el punto (1 o 2): ")
    
    if ganador_punto == "1":
        if puntos_jugador1 == 0:
            puntos_jugador1 = 15
        elif puntos_jugador1 == 15:
            puntos_jugador1 = 30
        elif puntos_jugador1 == 30:
            puntos_jugador1 = 40
        elif puntos_jugador1 == 40:
            print(f"{jugador1} ha ganado el juego.")
            break
    elif ganador_punto == "2":
        if puntos_jugador2 == 0:
            puntos_jugador2 = 15
        elif puntos_jugador2 == 15:
            puntos_jugador2 = 30
        elif puntos_jugador2 == 30:
            puntos_jugador2 = 40
        elif puntos_jugador2 == 40:
            print(f"{jugador2} ha ganado el juego.")
            break
    else:
        print("Opción inválida. Por favor ingrese 1 o 2.")
        continue

    seguir_jugando = input("¿Desea seguir jugando? (s/n): ")
    if seguir_jugando.lower() == "n":
        break

print(f"Puntuación final: {jugador1}: {puntos_jugador1} - {jugador2}: {puntos_jugador2}")