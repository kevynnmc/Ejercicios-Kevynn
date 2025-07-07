#para hackerram
def getMoneySpent(keyboards, drives, b):
    max_gasto = -1
    for k in keyboards:
        for d in drives:
            total = k + d
            if total <= b and total > max_gasto:
                max_gasto = total
    return max_gasto

#para visual
b, n, m = map(int, input("Presupuesto, cantidad de teclados y USBs: ").split())
keyboards = list(map(int, input("Precios de teclados: ").split()))
drives = list(map(int, input("Precios de USBs: ").split()))

resultado = getMoneySpent(keyboards, drives, b)

print(f"Máximo gasto posible: {resultado}")