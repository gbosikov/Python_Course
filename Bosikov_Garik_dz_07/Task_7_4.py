from os import walk
from os.path import join
from os.path import getsize
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def file_size_list(dir_path:str)->list:
    """
    Принемает в качестве аргумента пкть до директории
    :param dir_path: Путь до директории
    :return: список файлов размер которых больше 0
    """
    size = []
    for root, dirs, files in walk(dir_path):
        if not files:
            continue
        size.extend(getsize(join(root, name)) for name in files if int(getsize(join(root, name)) > 0))
    return size

# print(file_size_list(BASE_DIR))

size_range = [10 ** i for i in range(2, len(file_size_list(BASE_DIR)) + 1)]
dict_out = {}
for item in file_size_list(BASE_DIR):
    for key in size_range:
        if item < key:
            dict_out.update({key: dict_out.setdefault(key, 0) + 1})
            break

print(dict_out)

