def convert_list_in_str(list_in: list) -> str:
    """Обособляет каждое целое число кавычками, добавляя кавычку до и после элемента
        списка, являющегося числом, и дополняет нулём до двух целочисленных разрядов.
        Формирует из списка результирующую строковую переменную и возвращает."""
    check_list = []
    for num, element in enumerate(my_list):
        clean_list = []
        if element.isdigit():
            clean_list.append('"')
            clean_list.append(element.zfill(2))
            clean_list.append('"')
        elif element[0] in '+-':
            clean_list.append('"')
            clean_list.append(element.zfill(3))
            clean_list.append('"')
        else:
            clean_list.append(element)
        check_list.append(''.join(clean_list))

    str_out = print(str(f'{check_list[0]} {check_list[1]} {check_list[2]} {check_list[3]} {check_list[4]} {check_list[5]} {check_list[6]} {check_list[7]} {check_list[8]} {check_list[9]} '))
    return str_out


my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)