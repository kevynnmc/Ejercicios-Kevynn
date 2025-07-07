#para hackerram
def contarValles(pasos, ruta):
    nivel_mar = 0
    altitud = 0
    valles = 0

    for paso in ruta:
        if paso == 'U':
            altitud += 1
        else:
            altitud -= 1

        if paso == 'U' and altitud == 0:
            valles += 1

    return valles

#para visual
pasos = int(input("Ingrese el número total de pasos: "))
ruta = input("Ingrese la ruta (use 'U' para subir y 'D' para bajar): ").strip().upper()

resultado = contarValles(pasos, ruta)
print(f"Cantidad de valles recorridos: {resultado}")