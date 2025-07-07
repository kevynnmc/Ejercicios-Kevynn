import random

opciones = ["Piedra", "Papel", "Tijera"]

print("Juego de Piedra, Papel o Tijera")
rondas = int(input("¿Cuántas rondas quieres jugar? "))

puntaje_j = 0
puntaje_c = 0

for i in range(1, rondas + 1):
    print(f"Ronda {i} de {rondas}")
    print("Elige tu jugada:")
    print("1 - Piedra")
    print("2 - Papel")
    print("3 - Tijera")
    
    eleccion = input("Ingresa el número de tu jugada: ")
    if eleccion not in ["1", "2", "3"]:
        print("Jugada inválida. Pierdes esta ronda.")
        puntaje_c += 1
        continue
    
    jugada = opciones[int(eleccion) - 1]
    compu = random.choice(opciones)
    
    print("Jugador:", jugada)
    print("Computadora:", compu)
    
    if jugada == compu:
        print("Empate.")
    elif (jugada == "Piedra" and compu == "Tijera") or \
         (jugada == "Papel" and compu == "Piedra") or \
         (jugada == "Tijera" and compu == "Papel"):
        print("Ganaste esta ronda.")
        puntaje_j += 1
    else:
        print("La computadora gana esta ronda.")
        puntaje_c += 1
        
    print(f"Puntaje: Jugador {puntaje_j} - Computadora {puntaje_c}")

print(" Resultado final ")
if puntaje_j > puntaje_c:
    print("Ganaste el juego! Felicidades.")
elif puntaje_j < puntaje_c:
    print("La computadora ganó esta vez. ¡Inténtalo de nuevo!")
else:
    print("El juego terminó empatado.")



