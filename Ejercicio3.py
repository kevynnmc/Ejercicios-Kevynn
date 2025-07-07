import random

ganadas = 0
perdidas = 0

print("¡Bienvenido al juego contra la banca!")
print("Se reparten cartas con valores del 1 al 13.")
print("Ganas la ronda si tu carta es mayor que la de la banca.")
print("El juego termina si pierdes 3 veces, ganas 5 o decides retirarte.")

while True:
    decision = input("¿Quieres jugar esta ronda? (si/no): ").lower()
    if decision != 'si':
        print("Te has retirado del juego.")
        break

    carta_jugador = random.randint(1, 13)
    carta_banca = random.randint(1, 13)

    print(f"Tu carta: {carta_jugador} | Carta de la banca: {carta_banca}")

    if carta_jugador > carta_banca:
        ganadas += 1
        print("¡Ganaste esta ronda!")
    elif carta_jugador < carta_banca:
        perdidas += 1
        print("Perdiste esta ronda.")
    else:
        print("Empate. Nadie gana esta ronda.")

    if ganadas == 5:
        print("¡Felicidades! Has ganado 5 rondas. Eres el vencedor.")
        break
    if perdidas == 3:
        print("Has perdido 3 veces. La banca gana esta vez.")
        break

print(f"Resultado final: {ganadas} ganadas, {perdidas} perdidas.")
