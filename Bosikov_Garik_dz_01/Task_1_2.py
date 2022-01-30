"""""
Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
b) К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
*c) Решить задачу под пунктом b, не создавая новый список. (если будете решать - либо создайте доп. функцию, либо перепишите существующую sum_list_2)
"""""

my_list = [i ** 3 for i in range(1, 1000, 2)]  # создал список кубов нечётных чисел от 1 до 1000

# считаю сумму цифр
def digits_sum(digit):
    value = 0
    while digit != 0:
        value = value + digit % 10
        digit = digit // 10
    return value

# print(digits_sum(27))

def sum_list_1(dataset: list) -> int:
    # Вычисляет сумму чисел списка dataset, сумма цифр которых делится нацело на 7
    sum_7 = 0
    new_list = []
    for element in dataset:
        element_digits_sum = digits_sum(element)
        if element_digits_sum % 7 == 0:
            new_list.append(element)
    for new_element in new_list:
        sum_7 = sum_7 + new_element
    return sum_7

# print(sum_list_1([7,77]))

def sum_list_2(dataset: list) -> int:
    """К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
    сумма цифр которых делится нацело на 7"""
    sum2 = 0
    list3 = []
    for elem in dataset:
        new_number = elem + 17
        b = digits_sum(new_number)
        if b % 7 == 0:
            list3.append(new_number)
    for elem in list3:
        sum2 += elem
    return sum2


result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)


