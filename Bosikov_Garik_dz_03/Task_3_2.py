def num_translate_adv(value: str) -> str:
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
    rus_val = ''
    for key in some_dict.keys():
        if value == key:
            rus_val = some_dict.get(value)
        elif value == key.capitalize():
            rus_val = some_dict.get(key).capitalize()
    str_out = rus_val

    return str_out


print(num_translate_adv("one"))
print(num_translate_adv("eight"))
print(num_translate_adv("Five"))
