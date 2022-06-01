import sys


class OnlyInt(Exception):
    def __init__(self, txt):
        print('В списке должны быть только числа!')

    @staticmethod
    def check(list_in: list) -> bool:
        return False if sum([True for i in list_in if not str(i).isnumeric()]) > 0 else True


print('Введите числа, которые нужно добавить в список. Можно вводить несколько \
чисел через пробел. Введите "end" для преобразования.')

list_out = list()
for line in sys.stdin:
    if line.rstrip('\n') == 'end':
        break
    try:
        i = line.split()
        if OnlyInt.check(i) == False:
            raise OnlyInt(i)
        else:
            list_out.extend(i)
    except OnlyInt as e:
        pass

print(f'Получился список: {list_out}')
