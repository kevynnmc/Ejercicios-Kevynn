#para hackerram
def pageCount(numero, pagina):
    from_front = pagina // 2
    from_back = (numero // 2) - (pagina // 2)
    return min(from_front, from_back)

