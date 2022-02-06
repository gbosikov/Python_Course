"""
Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
Например:
# >>> num_translate("one")
"один"
# >>> num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None.
Подумайте, как и где лучше хранить информацию, необходимую для перевода: какой тип данных выбрать,
в теле функции или снаружи.
"""
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'


def num_translate(value: str) -> str:
    """переводит числительное с английского на русский """
    some_dict = {
        "zero": 'ноль',
        "one": 'один',
        "two": 'два',
        "three": 'три',
        "four": 'четыре',
        "five": 'пять',
        "six": 'шесть',
        "seven": 'семь',
        "eight": 'восемь',
        "nine": 'девять',
        "ten": 'десать'
    }
    # for key in some_dict.keys():
    #     if value == key:
    #         str_out = some_dict.get(value)
    str_out = some_dict.get(value)

    return str_out


print(num_translate("one"))
print(num_translate("eight"))
print(num_translate("Five"))
