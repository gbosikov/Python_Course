import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

p_folder = 'my_project'
child_folder1 = 'settings'
child_folder2 = 'mainapp'
child_folder3 = 'adminapp'
child_folder4 = 'authapp'

dir_name1 = os.path.join(BASE_DIR, p_folder)
os.makedirs(dir_name1, exist_ok=True)
dir_name2 = os.path.join(dir_name1, child_folder1)
os.makedirs(dir_name2, exist_ok=True)
dir_name3 = os.path.join(dir_name1, child_folder2)
os.makedirs(dir_name3, exist_ok=True)
dir_name4 = os.path.join(dir_name1, child_folder3)
os.makedirs(dir_name4, exist_ok=True)
dir_name5 = os.path.join(dir_name1, child_folder4)
os.makedirs(dir_name5, exist_ok=True)

