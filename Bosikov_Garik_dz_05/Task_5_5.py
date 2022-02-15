def get_uniq_numbers(src: list):
    return [val for val in src if src.count(val) == 1]


src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(*get_uniq_numbers(src))



