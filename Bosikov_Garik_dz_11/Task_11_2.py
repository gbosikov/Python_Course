# Задание 2


class DevisionByZero(Exception):
    __default_msg = 'Деление на ноль!!!'

    def __init__(self, msg=None):
        if msg:
            self.__default_msg = msg

    def __str__(self):
        return f'Недопустимая операция: {self.__default_msg}'


if __name__ == '__main__':
    try:
        args = input('Введите делимое и делитель через пробел: \n')
        a, b = map(float, args.split())
        if not b:
            raise DevisionByZero()
        print(a / b)
    except DevisionByZero as err:
        print(err)
