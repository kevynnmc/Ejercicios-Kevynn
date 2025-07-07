total = 0

print("Bienvenido a la máquina expendedora.")
print("1. Café ($3000) 2. Té ($2500) 3. Jugo ($3500)")
print("Ingresa 0 cuando ya no quieras pedir más.")

while True:
    opcion = int(input("¿Qué deseas tomar? (1-3 o 0 para salir): "))

    match opcion:
        case 1:
            print("Has elegido café. Valor: $3000\n")
            total += 3000
        case 2:
            print("Has elegido té. Valor: $2500\n")
            total += 2500
        case 3:
            print("Has elegido jugo. Valor: $3500\n")
            total += 3500
        case 0:
            print("Gracias por tu compra.")
            break
        case _:
            print("Opción no válida. Intenta nuevamente.")

print(f"Total a pagar: ${total}")
