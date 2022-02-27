import os
from Task_7_1 import BASE_DIR


def file_size_list(dir_path: str) -> list:
    """
    Принемает в качестве аргумента пкть до директории
    :param dir_path: Путь до директории
    :return: список файлов размер которых больше 0
    """
    size = []
    for root, dirs, files in os.walk(dir_path):
        if not files:
            continue
        size.extend(os.path.getsize(os.path.join(root, name))
                    for name in files if int(os.path.getsize(os.path.join(root, name)) > 0))
    return size

# print(file_size_list(BASE_DIR))

size_range = [10 ** i for i in range(2, len(file_size_list(BASE_DIR)) + 1)]
dict_out = dict()
for item in file_size_list(BASE_DIR):
    for key in size_range:
        if item < key:
            dict_out.update({key: dict_out.setdefault(key, 0) + 1})
            break

print(dict_out)

