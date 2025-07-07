#para hackerram
def pageCount(n, p):
    from_front = p // 2
    from_back = (n // 2) - (p // 2)
    return min(from_front, from_back)

