def get_uniq_numbers(src: list):
    unique = set()
    tmp = set()
    for el in src:
        if el not in tmp:
            unique.add(el)
        else:
            unique.discard(el)
        tmp.add(el)
    unique_ord = [el for el in src if el in unique]

    return list(unique_ord)


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))



