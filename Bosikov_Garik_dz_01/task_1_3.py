def transform_string(number: int) -> str:
    """Возвращает строку вида 'N процентов' с учётом склонения по указанному number"""
    lst = [2, 3, 4]
    out = str
    if number == 1:
        out = f'{number} {a}'
    elif number in lst:
        out = f'{number} {b}'
    elif number in range(4, 101):
        out = f'{number} {c}'

    return out


for n in range(1, 101):  # по заданию учитываем только значения от 1 до 100
    print(transform_string(n))