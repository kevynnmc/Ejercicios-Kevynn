#para hackerram
def pageCount(n_Total, pagina):
    from_front = pagina // 2
    from_back = (n_Total // 2) - (pagina // 2)
    return min(from_front, from_back)

