#para hackerram
def sockMerchant(n, ar):
    color_counts = {}
    pairs = 0

    for color in ar:
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    for count in color_counts.values():
        pairs += count // 2

    return pairs

