import sys


def add(argv):
    file1 = 'bakery.csv'
    if len(argv) != 2:
        print('Неверное количество аргументов\n')
    with open(file1, 'a', encoding='utf-8') as fa:
        fa.write(f'{argv}\n')


if __name__ == '__main__':
    sys.exit(add(sys.argv))
