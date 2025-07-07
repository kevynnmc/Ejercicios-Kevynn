#para hackerram
def pageCount(n, p):
    from_front = p // 2
    from_back = (n // 2) - (p // 2)
    return min(from_front, from_back)

#para visual
n = int(input("Introduce el número total de páginas: "))
p = int(input("Introduce la página que quieres abrir: "))

resultado = pageCount(n, p)
print(f"Número mínimo de movimientos: {resultado}")