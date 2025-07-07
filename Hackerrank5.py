#para hackerram
def getMoneySpent(keyboards, drives, b):
    max_gasto = -1
    for k in keyboards:
        for d in drives:
            total = k + d
            if total <= b and total > max_gasto:
                max_gasto = total
    return max_gasto

