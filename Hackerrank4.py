#para hackerram
def contarValles(pasos, ruta):
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

