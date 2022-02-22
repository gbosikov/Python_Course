import  sys


MAX_LEN = 10


def show(argv):
    if len(argv) == 1:
        with open('bakery.csv', 'r', encoding='utf-8') as fr:
            for line in fr:
                fr.seek()
                print(line.strip())
    elif len(argv) == 2:
        with open('bakery.csv', 'r', encoding='utf-8') as fr:
            fr.seek(((MAX_LEN + 2) * (int(argv[1]))), 0)
            for line in fr:
                print(line.strip())
    elif len(argv) == 3:
        with open('bakery.csv', 'r', encoding='utf-8') as fr:
            fr.seek(((MAX_LEN + 2) * (int(argv[1]))), 0)
            for index, line in enumerate(fr):
                print(line.strip())
                if index == int(argv[2]) - int(argv[1]):
                    break
    else:
        print('Please enter only two arguments')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(show(sys.argv))