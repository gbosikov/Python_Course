import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


with open('config.yaml', encoding='utf-8') as cfg:
    for line in cfg.readlines():
        if line.find('|') == 0:
            main_dir_path = os.path.join(BASE_DIR, line.replace('|', '').replace('-', '').strip())
            os.makedirs(main_dir_path, exist_ok=True)
        elif line.find('|') == 3:
            sub_dir_path = os.path.join(main_dir_path, line.replace('|', '').replace('-', '').strip())
            os.makedirs(sub_dir_path, exist_ok=True)
        elif line.find('|') == 6:
            sub_dir_path_lvl2 = os.path.join(sub_dir_path, line.replace('|', '').replace('-', '').strip())
            f_name = line.replace('|', '').replace('-', '').strip()
            if f_name.endswith('.py'):
                with open(os.path.join(sub_dir_path, f'{f_name}'), 'w') as py:
                    py.close()
            elif f_name.endswith('.html'):
                with open(os.path.join(sub_dir_path, f'{f_name}'), 'w') as html:
                    html.close()
            else:
                os.makedirs(sub_dir_path_lvl2, exist_ok=True)
        elif line.find('|') == 9:
            sub_dir_path_lvl3 = os.path.join(sub_dir_path_lvl2, line.replace('|', '').replace('-', '').strip())
            os.makedirs(sub_dir_path_lvl3, exist_ok=True)
        elif line.find('|') == 12 and line.replace('|', '').replace('-', '').strip().endswith('.html'):
            f_name1 = line.replace('|', '').replace('-', '').strip()
            with open(os.path.join(sub_dir_path_lvl3, f'{f_name1}'), 'w') as html:
                html.close()


"""
накостылил можно было создать функцию которая принемает путь к файлу и читает его
"""