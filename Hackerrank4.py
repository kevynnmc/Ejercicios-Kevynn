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

