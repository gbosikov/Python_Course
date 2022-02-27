import os
import shutil
from Task_7_1 import BASE_DIR

def my_func(p:str):
    """
    принимат путь к директории и создаёт папку templates, содержащую все шаблоны проэкта
    :param p: путь к проэкту
    :return: создает папку templates, содержащую все шаблоны проекта
    """
    if not os.path.exists(p):
        print('Directory not found')
        return 1
    for path, dirs, files in os.walk(p):
        if files:
            for f_name in files:
                if f_name.endswith('.html'):
                    try:
                        s_path = os.path.join(path, f_name)
                        d_path = os.path.join(p, 'templates')
                        os.makedirs(d_path, exist_ok=True)
                        new_path1 = os.path.join(d_path, 'authapp')
                        os.makedirs(new_path1, exist_ok=True)
                        new_path2 = os.path.join(d_path, 'mainapp')
                        os.makedirs(new_path2, exist_ok=True)
                        shutil.copy2(s_path, new_path1)
                        shutil.copy2(s_path, new_path2)
                    except shutil.SameFileError:
                        print(f'File {f_name} already exists')

a = os.path.join(BASE_DIR, 'my_project')
print(my_func(a))
