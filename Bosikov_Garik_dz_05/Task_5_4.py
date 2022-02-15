def get_numbers(src: list):
    out = list(src[j] for j in range(len(src)) if src[j] > src[j - 1] and j != 0)
    return out

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(*get_numbers(src))



